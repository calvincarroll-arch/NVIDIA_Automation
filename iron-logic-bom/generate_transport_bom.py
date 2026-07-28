#!/usr/bin/env python3
"""
Iron Logic Metro Transport BOM Generator (Smart Inventory Selection)
Dynamically selects hardware profiles based on deployment requirements.
"""

import json
import logging
import sys

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_config(filename="metro_transport_config.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.critical(f"Missing {filename}. Ensure you are in the 'iron-logic-bom' directory.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.critical(f"Corrupted JSON in {filename}: {e}")
        sys.exit(1)

def generate_transport_bom(deployment_type="compact", metro_nodes=3):
    hardware_db = load_config()
    logging.info(f"Generating Metro BOM for '{deployment_type}' profile with {metro_nodes} access nodes...")
    
    bom_output = {
        "domain": "Metro Carrier Transport (-48V DC Power)",
        "profile": deployment_type,
        "components": {},
        "totals": {
            "dc_power_draw_watts": 0,
            "total_rack_units": 0,
            "rack_utilization_percent": 0.0
        }
    }

    try:
        # --- THE SWITCH: This is what reads your request and grabs the right gear ---
        if deployment_type == "compact":
            transport_key = "CIENA_6500_2SLOT_PACKET_OPTICAL"
            quantity = 1
        elif deployment_type == "core":
            transport_key = "CIENA_6500_14SLOT_OTN"
            quantity = 1
        else:
            raise ValueError(f"Invalid deployment type: {deployment_type}")

        bom_output["components"][transport_key] = {"quantity": quantity}
        
        # Add Metro Access Edge
        metro_key = "FUJITSU_1FINITY_T100"
        bom_output["components"][metro_key] = {"quantity": metro_nodes}

        # Add Fiber Patch Panel & BDFB
        panel_key = "CORNING_FIBER_PATCH_PANEL_144"
        bom_output["components"][panel_key] = {"quantity": 1}

        bdfb_key = "ALPHA_TECHNOLOGIES_COMPACT_BDFB"
        bom_output["components"][bdfb_key] = {"quantity": 1}

        # --- Aggregate Math Calculations ---
        total_power = (
            (quantity * hardware_db[transport_key]["power_watts"]) +
            (metro_nodes * hardware_db[metro_key]["power_watts"]) +
            (1 * hardware_db[panel_key]["power_watts"]) +
            (1 * hardware_db[bdfb_key]["power_watts"])
        )

        total_rus = (
            (quantity * hardware_db[transport_key]["ru"]) +
            (metro_nodes * hardware_db[metro_key]["ru"]) +
            (1 * hardware_db[panel_key]["ru"]) +
            hardware_db[bdfb_key]["ru"]
        )

        STANDARD_RACK_RU = 42
        utilization = round((total_rus / STANDARD_RACK_RU) * 100, 1)

        bom_output["totals"]["dc_power_draw_watts"] = total_power
        bom_output["totals"]["total_rack_units"] = total_rus
        bom_output["totals"]["rack_utilization_percent"] = utilization

        return json.dumps(bom_output, indent=4)

    except (KeyError, ValueError) as e:
        logging.error(f"Configuration or deployment error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("\n--- IRON LOGIC SMART INVENTORY TRANSPORT BOM ---")
    # To use the big core gear in 4 months, just change "compact" to "core" right here:
    print(generate_transport_bom(deployment_type="compact", metro_nodes=3))
    print("------------------------------------------------\n")