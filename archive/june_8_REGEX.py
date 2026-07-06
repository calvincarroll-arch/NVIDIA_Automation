# import re

# log_line = "BGP Peer 192.168.100.254 established connection in 45 milliseconds"
# codes = re.findall(r' in (\d+)', log_line)

# print(codes)

# log_line = "System-Status: 99"
# shitsNgiggles = re.findall(r'Status:.(\d+)', log_line)

# print(shitsNgiggles)

# log_line = "CRITICAL: Missed keepalive counter has reached threshold [4/10]"
# count = re.findall(r'threshold \[(.+?)/', log_line)

# print(count)

import re

# log_line = "Driver Version: 2"

# result = re.search(r'Version: [12]', log_line)

# if result:
#     print("Match found!")
# else:
#     print("No match.")


# log_line = "Driver Version: 2"

# result = re.search(r'Version: [12]', log_line)

# if result:
#     print("Match found!")
# else:
#     print("No match.")

log_line = "Driver Version: 1"
result = re.search(r'Version: ([12])', log_line) # Added () around the [12]

if result:
    print(f"Match found! The version is: {result.group()}")

import re

# Scenario: An email is inside a log. You need it gone before it hits your AI agent.
log = "Received an email for go_nuts95@my.example.com"
pattern = r"[\w.%+-]+@[\w.-]+"

# The Eraser: Find the email, replace it with [REDACTED]
clean_log = re.sub(pattern, "[REDACTED]", log)
print(clean_log) 
# Output: Received an email for [REDACTED]