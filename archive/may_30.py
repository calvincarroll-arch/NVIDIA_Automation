# print(f"Hello New World")
# text = "Nvidia"
# print(text[0:3])
# x = "Dallas"
# print(x)
# x = 10
# print(x*2)

items = ["router", "swtich", "server"]
print(items[0])
items[0] = "firewall"
print(items[0])
items.append("cable")
print(items)
items.pop()
print(items)
# print(items[5])

for item in items:
    print(item[0:2])

