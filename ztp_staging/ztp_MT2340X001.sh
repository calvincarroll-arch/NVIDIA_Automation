#!/bin/sh
# --- IRON LOGIC DAY 0 ZTP BOOTSTRAP FOR MT2340X001 ---
# Site: dfw-ai-01 | Rack: DFW-RK-06

echo "[ZTP] Starting automated onboarding for MT2340X001..."

# Set Hostname
hostnamectl set-hostname dfw-leaf-06

# Configure Management Out-of-Band IP
nv set interface eth0 ip address 10.255.0.6/24

# Enable BGP Underlay ASN
nv set router bgp autonomous-system 65106

# Commit Day 0 Baseline
nv config apply -y

echo "[ZTP] Hardware MT2340X001 successfully bootstrapped!"
exit 0
