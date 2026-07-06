#!/usr/bin/env python3
"""
Iron Logic AI-Infra Toolkit
Module: BGP Keepalive Log Parser
Description: Ingests production switch/peer daemon logs to calculate real-world 
             missed keepalive rates and track protocol stability boundaries.
"""

import os
import sys

def parse_bgp_fabric_log(log_path):
    """
    Parses live telemetry streams to evaluate peer flap occurrences.
    """
    print(f"[*] Initializing Iron Logic BGP Fabric Audit on: {log_path}")
    
    if not os.path.exists(log_path):
        print(f"[!] ERROR: Target log path '{log_path}' cannot be located.")
        sys.exit(1)

    # State tracking boxes
    max_streak = 0
    total_warnings = 0
    session_collapsed = False

    print("[+] Log context acquired. Parsing state boundaries...")
    
    with open(log_path, 'r') as log_file:
        for line in log_file:
            line = line.strip()
            
            # Catch missed packets and extract integers safely
            if "Missed keepalive" in line:
                total_warnings += 1
                parts = line.split("Counter: ")
                if len(parts) > 1:
                    current_count = int(parts[1])
                    if current_count > max_streak:
                        max_streak = current_count
            
            # Catch critical terminal failures
            elif "CRITICAL" in line:
                session_collapsed = True

    print("-" * 80)
    print(f"[OK] Fabric Audit Concluded for Peer Target.")
    print(f" -> Peak Consecutive Keepalive Drop Streak: {max_streak}")
    print(f" -> Total Packet Warning Incidents Logged: {total_warnings}")
    print(f" -> Hard Session Teardown Triggered: {session_collapsed}")

if __name__ == "__main__":
    # Targets the persistent background daemon file directly
    target_log = "production/bgp_daemon.log"
    parse_bgp_fabric_log(target_log)