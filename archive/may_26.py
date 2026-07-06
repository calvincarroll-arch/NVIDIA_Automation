# fabric_name = "InfiniBand"
# if "band" in fabric_name:
#     print(fabric_name.upper())
# else:
#     print("Match failed")

# train = ["Apple", "Banana", "Cherry", "Date"]
# print(train[3])

# sentence = "Mom loves cooking"
# train = sentence.split()

# def get_word(sentence, n):
#     train = sentence.split()
#     return train[n-1]
# print(get_word("Now we are cooking!", 4))

# fruits = ["Strawberry", "Blueberry", "Raspberry", "Blackberry"]
# print(fruits[2])

# fruits = ["Strawberry", "Blueberry", "Raspberry"]
# fruits[1] = "Mango"
# print(fruits[1])

# servers = ["Node-A", "Node-B", "Node-C"]
# servers[0] = "Node-X"

# servers = ["Node-X", "Node-B", "Node-C"]
# servers.append("Node-D")
# print(servers)

# tools = []
# tools.append("Wireshark")
# tools.append("VS Code")
# print(tools)

# fabric = ["InfiniBand"]
# fabric.append("Ethernet")
# fabric[0] = "Spectrum-X"
# print(fabric)

# fabric.insert(1, "RoCEv2")
# print(fabric)

# fabric.remove("Ethernet")
# print(fabric)

# fabric.pop(0)
# print(fabric)

# interfaces = ["Ethernet0", "Ethernet1", "InfiniBand0"]
# for shitsNgiggles in interfaces:
#     print(f"Configuring interface: {shitsNgiggles}") 

# total_ports = len(interfaces)
# print(f"Total inventory count: {total_ports}")

# print(interfaces[-1])


# my_tuple = ("Router-A", "Router-B")
# secure_ports = (22, 80, 443)
# print(secure_ports[2])

# network_train = [
#     ("Core-Switch", "10.0.0.1"),
#     ("Edge-Router", "10.0.0.2")
# ]

# # You set up your 2 baskets right here: device and ip
# for shit, giggle in network_train:
#     print(f"Pinging {shit} at address {giggle}...")

# for packets in network_train:
#     print(f"Device: {packets[0]} | IP Address: {packets[1]}")

# winners = ["Ashley", "Dylan", "Reese"]

# for index, person in enumerate(winners):
# #     print(f"Slot {index} belongs to {person}")
# network_train = [
#     ("Core-Switch", "10.0.0.1"),
#     ("Edge-Router", "10.0.0.2")
# ]

# # Two custom baskets handle unpacking the nested values seamlessly
# for device, ip in network_train:
#     print(f"Pinging active host {device} at management IP {ip}")

# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)

# slots = ["1", "2", "3", "4"]
# clean_slots = [int(x) for x in slots]
# print(clean_slots)

# test_list = [x * 2 for x in range(3)]
# print(test_list)

z = [x for x in range(3)]
print(x)