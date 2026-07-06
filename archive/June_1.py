# # x = {}
# # type(x)
# # print(type(x))

# # file_counts = {"jph":10, "txt":14, "csv":2, "py":23}
# # print(file_counts)
# # print(file_counts["txt"])
# # "jpg" in file_counts
# # print()

# # file_counts["cfg"] = 8
# # print(file_counts)
# # for ext, amount in file_counts.items():
# #     print("There are {} files with the .{} extension".format(amount, ext))

# # uptime_report = {"RouterA": "45 days", "SwitchB": "120 days"}

# # for device, time in uptime_report.items():
# #     if device == "SwitchB":
# #         print(time)

# # uptime_report.keys()
# # uptime_report.values()

# # class Router:
# #     # The Constructor (Runs when creating the object)
# #     def __init__(self, hostname, ip):
# #         self.hostname = hostname  # Attribute
# #         self.ip = ip              # Attribute

# #     # Method (Action)
# #     def get_summary(self):
# #         return f"{self.hostname} ({self.ip})"

# # # Instantiate the object
# # r1 = Router("Core_R1", "10.1.1.1")
# # print(r1.get_summary())
# # max = Dog()

# # class Dog:
# #     def __init__(self, name, color):
# #         self.name = name
# #         self.color = color
# #     def bark(self):
# #         return f"{self.name} says WOOF!"
# #     def color_bark(self):
# #         return f"The {self.color} dog name {self.name} says WOOF!"
        

# # max = Dog("Max", "Brown")
# # print(max.name)
# # print(max.color)

# # rocky = Dog("Rocky", "Black")
# # print(max.color)
# # print(rocky.color)

# # print(max.bark())
# # print(rocky.bark())

# # print(max.color_bark())
# # print(rocky.color_bark())

# class Switch:
#     def __init__(self, hostname, ip, model):
#         self.hostname = hostname
#         self.ip = ip
#         self.model = model
#         self.vlans = []  # Starts with no extra VLANS

#     def add_vlan(self, vlan_id):
#         self.vlans.append(vlan_id)
#         return f"VLAN {vlan_id} added to {self.hostname}"
    
# class Switch:
#     # 1. The Assembly Line (Constructor)
#     def __init__(self, hostname, ip, model):
#         self.hostname = hostname   # Attribute
#         self.ip = ip               # Attribute
#         self.model = model         # Attribute
#         self.vlans = [1, 99]       # Attribute: Every switch starts with default VLANs

#     # 2. Action Method: Add a VLAN to this specific switch
#     def add_vlan(self, vlan_id):
#         if vlan_id not in self.vlans:
#             self.vlans.append(vlan_id)
#             return f"[SUCCESS] VLAN {vlan_id} added to {self.hostname}."
#         return f"[INFO] VLAN {vlan_id} already exists on {self.hostname}."

#     # 3. Action Method: Get a status report of the asset
#     def get_report(self):
#         return f"Device: {self.hostname} | IP: {self.ip} | Model: {self.model} | Active VLANs: {self.vlans}"


# # --- AUTOMATION ENGINE (Spinning up 50 Switches) ---

# network_inventory = []

# # Loop 50 times to create 50 unique physical assets dynamically
# for i in range(1, 51):
#     name = f"DFW-ASW-{i:02d}"          # Generates DFW-ASW-01, DFW-ASW-02...
#     ip_addr = f"10.100.10.{i}"         # Generates 10.100.10.1, 10.100.10.2...
    
#     # Instantiate the object using the blueprint
#     new_switch = Switch(hostname=name, ip=ip_addr, model="Cisco-9300")
    
#     # Add it to our network inventory list
#     network_inventory.append(new_switch)


# # --- TEST RUN: Let's touch the assets ---

# # Let's grab Switch #5 from our inventory and give it a specific config
# switch_five = network_inventory[4]  # Index 4 is the 5th switch
# print(switch_five.add_vlan(10))     # Provision VLAN 10 on it
# print(switch_five.add_vlan(20))     # Provision VLAN 20 on it

# print("-" * 50)

# # Let's run a quick discovery report on the first 7 switches in the rack
# for switch in network_inventory[:7]:
#     print(switch.get_report())

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")
print(car_makes)