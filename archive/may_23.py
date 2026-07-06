node_id = 0

while node_id < 5:
    node_id += 1  # Crucial: Increment BEFORE the continue check!
    
    # Let's say node 3 is a backup server we want to skip testing
    if node_id == 3:
        print("⚡ Node 3 is restricted. Skipping diagnostic lines below...")
        continue  # <-- Warps instantly back to the 'while' line!
        
    # This line is completely skipped when node_id is 3
    print(f"Running full diagnostics on Cluster Node-0{node_id}")


import random  # Borrowing our randomization toolbox to generate traffic data

# 1. DEFINE THE BLUEPRINT: Teach Python what 'check_packet' actually means
def check_packet(id_number):
    # Simulating a live firewall stream: 80% safe traffic, 20% threat anomalies
    traffic_types = ["Normal HTTPS Traffic", "Normal HTTPS Traffic", "MALICIOUS PAYLOAD"]
    return random.choice(traffic_types)

# 2. INITIALIZE TRACKING DATA
packet_id = 0

print("--- INITIALIZING FIREWALL PACKET SCAN ---")

# 3. CONTROL STREAM WITH CONTINUE INTERCEPT
while packet_id < 10:  # Scaled down to 10 for a clean output log
    packet_id += 1
    
    # Python executes our blueprint trick smoothly now!
    packet_type = check_packet(packet_id)
    
    if packet_type == "Normal HTTPS Traffic":
        continue  # SKIPS the alert print below, warps straight back to 'while' line
        
    # Execution ONLY reaches down here if the 'continue' was not triggered!
    print(f"⚠️ ALERT: Security anomaly flagged on Packet ID {packet_id}! [{packet_type}]")

print("--- SCAN COMPLETE ---")

n = 1
while n < 10:
    if n % 2 == 0:
        n += 3
    else:
        n += 1
print(n)

