#!/usr/bin/env python3
"""
Iron Logic BOM Generator
Calculates hardware, power, and space constraints for GPU localized fabrics.
"""

import json
import logging
import os

# 1. Initialize SRE Logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_hardware_config(filepath="config.json"):
    """Loads hardware definitions from an external JSON file."""
    try:
        # Context manager automatically closes the file when done
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.critical(f"Missing {filepath}. Cannot generate BOM without hardware data.")
        raise
    except json.JSONDecodeError as e:
        logging.critical(f"Corrupted JSON format in config file: {e}")
        raise

def generate_fabric_bom(num_nodes, gpus_per_node, hardware_db):
    """
    Calculates the BOM requirements based on node count and dynamic hardware DB.
    """
    logging.info(f"Generating BOM for {num_nodes} nodes with {gpus_per_node} GPUs each...")
    
    bom_output = {
        "fabric_specs": {
            "total_nodes": num_nodes,
            "total_gpus": num_nodes * gpus_per_node
        },
        "components": {},
        "totals": {
            "power_draw_watts": 0,
            "rack_units": 0
        }
    }

    try:
        # 3. Calculate GPU Compute
        gpu_key = "NVIDIA_H100_SXM"
        total_gpus = num_nodes * gpus_per_node
        bom_output["components"][gpu_key] = {"quantity": total_gpus}
        bom_output["totals"]["power_draw_watts"] += total_gpus * hardware_db[gpu_key]["power_watts"]

        # 4. Calculate Chassis Requirements
        chassis_key = "NVIDIA_HGX_8GPU_CHASSIS"
        bom_output["components"][chassis_key] = {"quantity": num_nodes}
        bom_output["totals"]["power_draw_watts"] += num_nodes * hardware_db[chassis_key]["power_watts"]
        bom_output["totals"]["rack_units"] += num_nodes * hardware_db[chassis_key]["ru"]

        # 5. Calculate Networking 
        switch_key = "MELLANOX_SN4600_SWITCH"
        num_switches = max(1, num_nodes // 4) 
        bom_output["components"][switch_key] = {"quantity": num_switches}
        bom_output["totals"]["power_draw_watts"] += num_switches * hardware_db[switch_key]["power_watts"]
        bom_output["totals"]["rack_units"] += num_switches * hardware_db[switch_key]["ru"]

        # 6. Convert Python Dictionary to formatted JSON string
        return json.dumps(bom_output, indent=4)

    except KeyError as e:
        logging.error(f"Hardware component not found in config.json: {e}")
        raise 
    except Exception as e:
        logging.critical(f"An unexpected error occurred during BOM generation: {e}")
        raise

if __name__ == "__main__":
    try:
        print("\n--- IRON LOGIC BOM GENERATOR V2 ---")
        
        # Load the database first
        hardware_data = load_hardware_config("config.json")
        
        # Pass the database into the generator
        generated_bom = generate_fabric_bom(num_nodes=4, gpus_per_node=8, hardware_db=hardware_data)
        
        print(generated_bom)
        print("-----------------------------------\n")
        logging.info("BOM generation completed successfully.")
    except Exception:
        logging.error("Failed to generate BOM. Check logs for details.")