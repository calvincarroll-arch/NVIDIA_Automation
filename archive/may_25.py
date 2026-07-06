# # print("Hello new world Im on my way")



# # index = 0
# # while index < 5:
# #     if index == 3:
# #         index += 2
# #         continue
# #     index += 1
# # print(index)

# # total = 10
# # while total > 2:
# #     total -= 3
# # print(total)

# # n = 5
# # while n < 25:
# #     print(n)
# #     n += 5

# # product = 1
# # x = 1
# # while x < 4:
# #     product = product * x
# #     x += 1

# # k = 10
# # while k > 5:
# #     k -= 1
# #     if k == 7:
# #         break
# # print(k)

# # for x in range(5):
# #     print(x)



# # friends = ['Taylor', 'Alex', 'Pat', 'Eli']
# # for friend in friends:
# #     print("Hi " + friend)

# # print("Hello New World")
# # print("\n--- Custom Start and Stop Boundaries ---")
# # # Starts exactly at 1, exits strictly BEFORE reaching 6
# # for port in range(1, 6):
# #     print("Auditing GigabitEthernet0/0/" + str(port))

# # print("\n--- Stepping Through Increments ---")
# # # Starts at 2, counts up to 10, jumping by 2 on each pass
# # for vlan in range(2, 11, 2):
# #     print("Configuring Allowed VLAN: " + str(vlan))
# # chicken_wings = ["Buffalo", "Lemon Pepper", "Garlic Parmesan", "BBQ"]

# # # We use len() to get the total count (4), so range(4) generates indexes: 0, 1, 2, 3
# # for planes in range(len(chicken_wings)):
# #     # We use brackets [planes] to pull the string out using its current number position
# #     print(f"Index {planes} matches wing flavor: {chicken_wings[planes]}")

# # # --- GLOBAL RUNTIME LEVEL (No Indentation) ---
# devices = ["router1", "router2", "router3"]

# for device in devices:
# #  |
# #  └───> COLON OPENS THE BOX
# #  |
# #  v   <--- 4 SPACES INJECTED (Inside the box)
#     print(f"Connecting to {device}...")
#     print("Pulling running configuration...")
#     # These 2 lines loop repeatedly!
# #  ^
# #  |
# #  └───> INDENTATION DROPS BACK TO ZERO (Box is closed)

# # nums = [1, 2, 3]
# # total = 0
# # for n in nums:
# #     total += n
# # print(total)
# # total = 0
# # for factor in range(1, 4):
# #     total = total * factor
# # print(total)

# # for x in range(5):
# #     if x == 3:
# #         break
# #     print(x)

# # # 
# # tracker = 10
# # for x in range(2):
# #     tracker += 5
# # tracker += 1
# # print(tracker)

# # for left in range(7):
# #     for right in range(left, 7):
# #         print("[" + str(left) + "|" + str(right) + "]", end=" " )
# #     print()


# # teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# # for home_team in teams:
# #     for away_teams in teams:
# #         if home_team != away_teams:
# #             print(home_team + " vs " + away_teams)

# # word = "Net"
# # for letter in word:
# #     print(letter.upper())

# # greeting = "Hello"
# # for i in range(len(greeting)):
# # 	print(i)
      
# nums = [1, 2, 3, 4]
# new_list = []
# for x in nums:
#     if x > 2:
#         new_list.append(x)

# for n in range(19):
#     if n % 2 == 0:
#         print(n)

# for n in range(18+1):
#     print(n**2)


# for x in range(1, 10, 3):
#     print(x)

# num1 = 0
# num2 = 0

# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y + 3

# print(num1 + num2)

# x = 1
# sum = 5
# while x <= 10:
#     sum += x
#     x += 1
# print(sum)

# int("12345") + int("54321")
# print(int("12345") + int("54321"))

# name = "Manny"
# print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

text = "Telemetry"
print(text[:])