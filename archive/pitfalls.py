def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)

def print_range(start, end):
    n = start
    while n <= end:
        print (n)
        n += 1

print_range(1, 5)


multiplier = 1
while multiplier <= 3:
    print(5 * multiplier)
    multiplier += 1


counter = 0
while counter < 5:
    print(f"Processing node batch...")
    counter += 1


gpu_count = 8
while gpu_count < 20:
    print(f"gpu_count {gpu_count}")
    gpu_count += 1
print(f"gpu_count {gpu_count}")

datacenter_region = "Dallas-Fort Worth"
offline_switches = 3

# Multiple magic windows in one clean line of code
alert_message = f"ALERT: The {datacenter_region} fabric has {offline_switches} down devices!"

print(alert_message)

import time 
import random

def simulate_ping_request():
    # Simulating a live network fabric event: 30% chance of success, 70% chance of drop
    statuses = ["Success", "Timeout", "Timeout"]
    return random.choice(statuses)

ping_success = False
attempt_counter = 0

while attempt_counter < 5 and not ping_success:
    attempt_counter += 1
    print(f"Sending ICMP ping to gateway... Attempt {attempt_counter}")

    response = simulate_ping_request()

    if response == "Success":
        ping_success = True
    else:
        print("Ping time out. Backing off for 2 seconds... ")
        time.sleep(2)

if ping_success:
    print("✅ Network Fabric Link Verified.")
else:
    print("❌ CRITICAL: Target Host Unreachable after 5 attempts.")


import time  # 1. Borrow the clock toolbox from the system

# 2. Define our custom function (The Blueprint)
def shout_warning():
    print("⚠️ LINK OFFLINE: Retrying...")

# 3. Initialize our tracking loop variables
retry_count = 0

# 4. Run our automated validation loop
while retry_count < 3:
    shout_warning()  # <-- Calling our secret trick here!
    
    time.sleep(2)    # <-- Using our imported clock tool to wait 2 seconds
    retry_count += 1 # <-- Adding 1 to our piggy bank counter

print("Process finished.")

x = 1
while x < 4:
    print(x, end=" ")
    x = x + 1
print("Done")



i = 1
while i < 3:
    j = 1
    while j < 3:
        print("X")
        j += 1
    i += 1





