#!/usr/bin/env python3
"""
Iron Logic AI Fabric BOM Generator
Calculates AC power, rack units, and hardware for localized high-performance compute.
"""

import json
import logging
import sys

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_config(filename="ai_fabric_config.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.critical(f"Missing {filename}. Ensure the AI config is present.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.critical(f"Corrupted JSON in {filename}: {e}")
        sys.exit(1)

def generate_ai_bom(num_nodes, gpus_per_node):
    hardware_db = load_config()
    logging.info(f"Calculating AI Compute Fabric BOM for {num_nodes} nodes ({gpus_per_node} GPUs/node)...")
    
    bom_output = {
        "domain": "AI Data Center (AC Power)",
        "fabric_specs": {
            "total_nodes": num_nodes,
            "total_gpus": num_nodes * gpus_per_node
        },
        "components": {},
        "totals": {
            "facility_power_draw_watts": 0,
            "total_rack_units": 0
        }
    }

    try:
        # 1. Compute Calculation (H100 or MI300X)
        gpu_key = "NVIDIA_H100_SXM"
        total_gpus = num_nodes * gpus_per_node
        bom_output["components"][gpu_key] = {"quantity": total_gpus}
        bom_output["totals"]["facility_power_draw_watts"] += total_gpus * hardware_db[gpu_key]["power_watts"]

        # 2. Chassis Calculation
        chassis_key = "NVIDIA_HGX_8GPU_CHASSIS"
        bom_output["components"][chassis_key] = {"quantity": num_nodes}
        bom_output["totals"]["facility_power_draw_watts"] += num_nodes * hardware_db[chassis_key]["power_watts"]
        bom_output["totals"]["total_rack_units"] += num_nodes * hardware_db[chassis_key]["ru"]

        # 3. Leaf/Spine Networking
        switch_key = "MELLANOX_SN4600_SWITCH"
        num_switches = max(1, num_nodes // 4)
        bom_output["components"][switch_key] = {"quantity": num_switches}
        bom_output["totals"]["facility_power_draw_watts"] += num_switches * hardware_db[switch_key]["power_watts"]
        bom_output["totals"]["total_rack_units"] += num_switches * hardware_db[switch_key]["ru"]

        return json.dumps(bom_output, indent=4)

    except KeyError as e:
        logging.error(f"Missing hardware key in AI configuration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("\n--- IRON LOGIC AI FABRIC BOM ---")
    print(generate_ai_bom(num_nodes=4, gpus_per_node=8))
    print("---------------------------------\n")

    