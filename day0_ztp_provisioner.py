import json
import os

# Simulated bare-metal hardware discovered during rack installation
NEW_DISCOVERED_SWITCHES = [
    {
        "serial": "MT2340X001",
        "mac": "00:02:C9:AB:CD:01",
        "model": "NVIDIA SN4600",
        "target_rack": "DFW-RK-06",
        "target_site": "dfw-ai-01",
        "asn": 65106,
        "mgmt_ip": "10.255.0.6/24"
    }
]

def generate_cumulus_ztp_script(switch_data):
    """
    Generates an executable Zero Touch Provisioning (ZTP) shell script
    that Cumulus Linux executes automatically on Day 0 boot.
    """
    ztp_script_content = f"""#!/bin/sh
# --- IRON LOGIC DAY 0 ZTP BOOTSTRAP FOR {switch_data['serial']} ---
# Site: {switch_data['target_site']} | Rack: {switch_data['target_rack']}

echo "[ZTP] Starting automated onboarding for {switch_data['serial']}..."

# Set Hostname
hostnamectl set-hostname dfw-leaf-06

# Configure Management Out-of-Band IP
nv set interface eth0 ip address {switch_data['mgmt_ip']}

# Enable BGP Underlay ASN
nv set router bgp autonomous-system {switch_data['asn']}

# Commit Day 0 Baseline
nv config apply -y

echo "[ZTP] Hardware {switch_data['serial']} successfully bootstrapped!"
exit 0
"""
    return ztp_script_content

def main():
    print("--- IRON LOGIC: AUTOMATED DAY 0 ZTP MANIFEST GENERATOR ---\n")
    
    os.makedirs("ztp_staging", exist_ok=True)
    
    for switch in NEW_DISCOVERED_SWITCHES:
        print(f"🔍 Discovered unprovisioned serial: {switch['serial']} (MAC: {switch['mac']})")
        print(f"📍 NetBox Target Mapping: {switch['target_site']} -> {switch['target_rack']} -> ASN {switch['asn']}")
        
        # Render the ZTP Boot Manifest
        ztp_manifest = generate_cumulus_ztp_script(switch)
        
        # Save to local staging directory for HTTP/PXE boot handoff
        filename = f"ztp_staging/ztp_{switch['serial']}.sh"
        with open(filename, "w") as f:
            f.write(ztp_manifest)
            
        print(f"🚀 Staged Day 0 ZTP boot file: {filename}\n")

if __name__ == "__main__":
    main()