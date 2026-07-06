#!/usr/bin/env python3
"""
Iron Logic AI-Infra Toolkit
Module: NCCL Optical Auditor
Description: Parses switch logs for fabric degradation patterns.
"""

import os
import re
import sys
import argparse

def audit_switch_logs(log_file_path):
    print(f"[*] Initializing Iron Logic Optical Auditor...")
    print(f"[*] Target Log File: {log_file_path}")
    
    if not os.path.exists(log_file_path):
        print(f"[!] ERROR: Target log file '{log_file_path}' not found.")
        sys.exit(1)
        
    # Define our hunt patterns (The "Bounty" list)
    # 1. Buffer Overflows, 2. Micro-reflections, 3. RDMA drops
    patterns = {
        "Buffer Overflow": r"buffer\s+overflow",
        "Micro-reflection": r"micro-reflection|symbol\s+error",
        "RDMA Packet Drop": r"rdma\s+drop|packet\s+loss"
    }
    
    print("[+] Log file acquired. Starting deep packet inspection...")
    
    # Open the log and iterate line-by-line
    with open(log_file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            for issue, regex in patterns.items():
                if re.search(regex, line, re.IGNORECASE):
                    print(f"[!] ALERT: Found {issue} on line {line_num}: {line.strip()}")

if __name__ == "__main__":
    # Initialize the argument parser 
    parser = argparse.ArgumentParser(description="Iron Logic NCCL Optical Auditor")
    
    # Add a mandatory argument for the log file path 
    parser.add_argument("log_file", help="Path to the switch log file for analysis")
    
    # Parse the arguments provided by the user in the terminal 
    args = parser.parse_args()

    # Pass the CLI argument directly to your auditor function 
    audit_switch_logs(args.log_file)

