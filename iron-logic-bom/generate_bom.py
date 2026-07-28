#!/usr/bin/env python3
"""
Iron Logic BOM Generator
Calculates hardware, power, and space constraints for GPU localized fabrics.
"""

import json
import logging

# 1. Initialize SRE Logging (Muting standard noise, tracking criticals)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# 2. The Hardware Database (Dictionaries)
# In Phase 2, we will move this to a separate config.json file!
HARDWARE_DB = {
    "NVIDIA_H100_SXM": {"power_watts": 700, "ru": 0, "type": "GPU"},
    "NVIDIA_HGX_8GPU_CHASSIS": {"power_watts": 2000, "ru": 8, "type": "Chassis"}, # Base chassis power
    "MELLANOX_SN4600_SWITCH": {"power_watts": 450, "ru": 2, "type": "Network"},
    "OSFP_800G_TRANSCEIVER": {"power_watts": 20, "ru": 0, "type": "Optics"}
}

def generate_fabric_bom(num_nodes, gpus_per_node):
    """
    Calculates the BOM requirements based on node count.
    """
    logging.info(f"Generating BOM for {num_nodes} nodes with {gpus_per_node} GPUs each...")
    
    # Initialize the output dictionary
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
        bom_output["totals"]["power_draw_watts"] += total_gpus * HARDWARE_DB[gpu_key]["power_watts"]

        # 4. Calculate Chassis Requirements
        chassis_key = "NVIDIA_HGX_8GPU_CHASSIS"
        bom_output["components"][chassis_key] = {"quantity": num_nodes}
        bom_output["totals"]["power_draw_watts"] += num_nodes * HARDWARE_DB[chassis_key]["power_watts"]
        bom_output["totals"]["rack_units"] += num_nodes * HARDWARE_DB[chassis_key]["ru"]

        # 5. Calculate Networking (Assume 1 Leaf switch per 4 nodes for this model)
        switch_key = "MELLANOX_SN4600_SWITCH"
        num_switches = max(1, num_nodes // 4) 
        bom_output["components"][switch_key] = {"quantity": num_switches}
        bom_output["totals"]["power_draw_watts"] += num_switches * HARDWARE_DB[switch_key]["power_watts"]
        bom_output["totals"]["rack_units"] += num_switches * HARDWARE_DB[switch_key]["ru"]

        # 6. Convert Python Dictionary to formatted JSON string
        final_json = json.dumps(bom_output, indent=4)
        return final_json

    # 7. Exception Handling (EAFP)
    except KeyError as e:
        logging.error(f"Hardware component not found in database: {e}")
        # Raising the error stops the script so we don't output a corrupted BOM
        raise 
    except Exception as e:
        logging.critical(f"An unexpected error occurred during BOM generation: {e}")
        raise

if __name__ == "__main__":
    try:
        print("\n--- IRON LOGIC BOM GENERATOR ---")
        # Let's generate a BOM for a standard 4-node cluster (32 GPUs)
        generated_bom = generate_fabric_bom(num_nodes=4, gpus_per_node=8)
        print(generated_bom)
        print("--------------------------------\n")
        logging.info("BOM generation completed successfully.")
    except Exception:
        logging.error("Failed to generate BOM. Check hardware database keys.")