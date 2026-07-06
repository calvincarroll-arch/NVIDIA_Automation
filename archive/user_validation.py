# 🛠️ production/user_validation.py
"""
Sovereign AI Infrastructure - User Input Validation Engine
Reconstructs the broken Coursera widget from image_3ff272.png into a working, 
local prototyping script. Demonstrates indefinite validation loops.
"""

def is_valid_vlan(vlan_input):
    """
    Validates if the user input is a mathematically valid IEEE 802.1Q VLAN ID.
    VLAN ID must be an integer between 1 and 4094.
    """
    try:
        vlan_id = int(vlan_input)
        # VLAN ID boundary constraint: 1 <= vlan_id <= 4094
        if 1 <= vlan_id <= 4094:
            return True
    except ValueError:
        # Handle non-integer inputs (like strings or letters) safely to prevent a crash
        pass
    return False

def get_vlan_configuration():
    """
    Prompts the operator to configure a network VLAN.
    Utilizes an indefinite while loop (State Trap) to force valid configuration.
    """
    print("[*] Launching VLAN Configuration Wizard...")
    
    # 1. Initial State Capture (Equivalent to the first get_username() in your reading)
    raw_input = input("Enter target VLAN ID (1-4094): ")
    
    # 2. The Indefinite Validation Gate
    # The loop continues to run AS LONG AS the validation check returns False
    while not is_valid_vlan(raw_input):
        print(f"[ERROR] '{raw_input}' is not a valid 802.1Q VLAN boundary.")
        print("[*] Please enter a valid integer within the designated range.")
        print("-" * 50)
        
        # 3. State Mutation: Prompt again inside the loop
        # Critical: Without this line, the loop becomes infinite because raw_input never changes!
        raw_input = input("Enter target VLAN ID (1-4094): ")
        
    # 4. Loop Exit Boundary (Only reachable once is_valid_vlan returns True)
    valid_vlan_id = int(raw_input)
    print("-" * 50)
    print(f"[SUCCESS] VLAN {valid_vlan_id} validated. Applying to switch fabric...")
    return valid_vlan_id

if __name__ == "__main__":
    # Execute the interactive console configuration wizard
    configured_vlan = get_vlan_configuration()
    print(f"\nFinal Fabric Assignment: VLAN {configured_vlan}")
#eof




