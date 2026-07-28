#!/usr/bin/env python3
"""
Iron Logic Optic Health & Port Mapping Auditor (Carrier Edition)
Parses Ciena-style shelf/slot/port (sh/sl/pt) nomenclature, validates 
optical power levels (dBm), and maps transport circuits.
"""

import json
import logging
import sys

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Telemetry modeled with Ciena shelf/slot/port (sh/sl/pt) naming conventions
CARRIER_OPTICS_TELEMETRY = {
    "1-3-1": {
        "card_type": "400G_Data_Muxponder",
        "transceiver": "QSFP-DD-400G",
        "state": "In-Service",
        "rx_power_dbm": -4.2,  # Healthy operational window
        "tx_power_dbm": -1.0,
        "circuit_id": "VC-TR-DALLAS-ASHBURN-01"
    },
    "1-3-2": {
        "card_type": "400G_Data_Muxponder",
        "transceiver": "QSFP-DD-400G",
        "state": "In-Service",
        "rx_power_dbm": -8.5,  # Degraded signal / high loss flag
        "tx_power_dbm": -1.2,
        "circuit_id": "VC-TR-DALLAS-CHICAGO-04"
    },
    "2-5-1": {
        "card_type": "100G_OTN_Line",
        "transceiver": "CFP2-ACO",
        "state": "OutOfService",
        "rx_power_dbm": -35.0, # Loss of Light / Unlit fiber
        "tx_power_dbm": -35.0,
        "circuit_id": "UNASSIGNED_SPARE"
    }
}

def audit_carrier_optics(telemetry_data):
    """
    Evaluates optical power thresholds against Ciena interface telemetry.
    """
    logging.info("Auditing carrier transport line cards and optical budgets...")
    
    audit_report = {
        "network_domain": "Metro Carrier Transport (Ciena 6500 / 1FINITY)",
        "healthy_links": [],
        "degraded_links": [],
        "unlit_ports": [],
        "circuit_cross_connect_map": {}
    }

    RX_DEGRADED_THRESHOLD = -7.0  # Threshold where chromatic dispersion or insertion loss hurts a circuit

    for port_id, metrics in telemetry_data.items():
        # Map out the circuit allocation using exact sh/sl/pt identifiers
        audit_report["circuit_cross_connect_map"][port_id] = {
            "circuit": metrics["circuit_id"],
            "hardware": metrics["card_type"]
        }

        # Analyze optical health
        if metrics["state"] == "OutOfService" or metrics["rx_power_dbm"] <= -30.0:
            audit_report["unlit_ports"].append({
                "shelf_slot_port": port_id,
                "circuit": metrics["circuit_id"],
                "status": "Loss of Signal (LoS) / Unlit"
            })
        elif metrics["rx_power_dbm"] < RX_DEGRADED_THRESHOLD:
            audit_report["degraded_links"].append({
                "shelf_slot_port": port_id,
                "circuit": metrics["circuit_id"],
                "rx_dbm": metrics["rx_power_dbm"],
                "warning": "High optical attenuation detected on line card"
            })
        else:
            audit_report["healthy_links"].append({
                "shelf_slot_port": port_id,
                "circuit": metrics["circuit_id"],
                "rx_dbm": metrics["rx_power_dbm"]
            })

    return json.dumps(audit_report, indent=4)

if __name__ == "__main__":
    print("\n--- IRON LOGIC CARRIER OPTIC AUDITOR ---")
    report = audit_carrier_optics(CARRIER_OPTICS_TELEMETRY)
    print(report)
    print("------------------------------------------\n")