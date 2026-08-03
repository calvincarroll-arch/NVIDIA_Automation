from nornir import InitNornir

# Initialize Nornir and point it to your config file
nr = InitNornir(config_file="day1_provisioning/inventory/config.yaml")

# Print the connection status
print("--- IRON LOGIC API TEST ---")
print("Successfully connected to NetBox!")
print(f"Currently tracking {len(nr.inventory.hosts)} devices in the inventory.")