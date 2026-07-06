print("NVIDIA Architect Online")
print(2+2/((2+2)+(2**2)))
import os

# THE SOURCE OF TRUTH: Your combined architectural insights
aha_moments = [
    {"ID": "#281", "Topic": "Localhost Server", "Aha": "The Terminal is the engine room, the Browser is just the dashboard."},
    {"ID": "#291", "Topic": "The Golden Image", "Aha": "A master template containing all known good configurations."},
    {"ID": "#308", "Topic": "Strategic Tooling", "Aha": "Adopt VS Code for its multi-language support and remote-development capabilities."},
    {"ID": "#309", "Topic": "AI Augmentation", "Aha": "Integrating Gemini Code Assist turns the IDE into an active collaborator for secure deployment."},
    {"ID": "#311", "Topic": "Workflow Distinction", "Aha": "ML Designer is for building intelligence; Prompt Flow is for directing and securing it."},
    {"ID": "#314", "Topic": "Module Execution Flow", "Aha": "Using 'python -m' acts as a fail-safe when the system 'map' (PATH) is broken."},
    {"ID": "#315", "Topic": "Interpreter vs. CLI", "Aha": "Launch software from the OS Terminal, not from within the Python '>>>' prompt."},
    {"ID": "#317", "Topic": "Localhost Handshake", "Aha": "A local web server creates a secure, air-gapped environment for rapid prototyping."}
]

# THE EXPORT LOGIC
filename = "NVIDIA_Prep_Notes.txt"

# This writes the file to the current folder you have open in Jupyter
with open(filename, 'w', encoding='utf-8') as file:
    file.write("--- IRON LOGIC LLC: NVIDIA SOLUTIONS ARCHITECT BRAIN DUMP ---\n\n")
    for moment in aha_moments:
        file.write(f"MOMENT {moment['ID']}\n")
        file.write(f"TOPIC: {moment['Topic']}\n")
        file.write(f"INSIGHT: {moment['Aha']}\n")
        file.write("-" * 50 + "\n\n")

print(f"✅ SUCCESS: {filename} has been updated in your local workspace.")
print(f"Hello new world Im on my way")
dallas_node_status = "Online"
total_active_gpus = 8
is_encryption_enabled = True

def check_sovereign_security():
    # RULE: Readability counts.
    if is_encryption_enabled == True:
        print("✅ SECURITY ALERT: Data is shielded.")
    else:
        print("⚠️ WARNING: Data is unencrypted.")

check_sovereign_security()
# 1. Keywords: 'if', 'print', 'and' are reserved words.
# 2. Operators: '>', '<', '==' perform the checks.

server_temp = 75  # Variable
max_safe_temp = 80 # Variable

# 3. An Expression: Calculating the "Safety Margin"
safety_margin = max_safe_temp - server_temp 

# 4. Conditional Statement: Making a decision
if server_temp > max_safe_temp:
    print("🔥 CRITICAL: Cooling failure! Shutting down.")
else:
    # We used an Operator (==) to check for a perfect 0 margin
    if safety_margin == 0:
        print("⚠️ WARNING: Running at the limit.")
    else:
        print("✅ STABLE: Current margin is " + str(safety_margin) + " de")
              
base = 6
height = 3
areas = (base*height)/2
print("The are of the triangle is: " + str(areas))             
print("I went to war last night!")
print(type(10.5))
print(type("Iron Logic"))
# 1. THE INPUTS (Data coming in as different types)
gpu_label = "NVIDIA-H100-Primary"  # This is a 'str'
raw_gpu_count = "8"                # This looks like a number, but it's a 'str'!
power_draw_per_gpu = 0.725         # This is a 'float' (Kilowatts)

# 2. THE CONVERSIONS (Putting on the Magic Hats)
# We can't do math with a string "8", so we force it into an 'int'
actual_count = int(raw_gpu_count)

# 3. THE EXPRESSION (The Math)
# Integer * Float = Float
total_power_needed = actual_count * power_draw_per_gpu

# 4. THE CLEANUP (The Haircut)
# Let's round it to 2 decimal places so it looks professional
final_report_power = round(total_power_needed, 2)

# 5. THE OUTPUT (The Megaphone)
print("--- IRON LOGIC INFRASTRUCTURE AUDIT ---")
print("Target: " + gpu_label)
print("Total Power Load: " + str(final_report_power) + " kW")

# 6. THE SAFETY CHECK (The Sorting Hat)
# Let's verify the types for our 'Aha!' log
print("\n[Technical Audit]")
print("Count Type: " + str(type(actual_count)))
print("Power Type: " + str(type(final_report_power)))
print("SERVER: OnlineSTATUS: Healthy")
# Output: SERVER: OnlineSTATUS: Healthy (Messy!)
print("SERVER: Online\nSTATUS: Healthy")
# Output:
# SERVER: Online
# STATUS: Healthy (Professional!)
def greeting(name):
    print("Welcome, " + name)

def check_rack_power(rack_name, current_draw):
    max_safe_draw = 15.0
    print("Checking Rack: " + rack_name)

    if current_draw > max_safe_draw:
        print("ALERT: " + rack_name + "is OVERLOADED! Draw: " + str(current_draw) + "kw")
    else:
        print("✅ STATUS: " + rack_name + " is safe. Draw: " + str(current_draw) + "kW")
    print("--------------------")

check_rack_power("DFW-NVIDIA-01", 12.5)
check_rack_power("DFW-NVIDIA-02", 18.2)
check_rack_power("DFW-NVIDIA-03", 9.4)
total_gpus = 10
print('Total GPUs: ' + str(total_gpus))

node = 'DFW-01'
status = 'Online'
print('Node' + node + 'is' + status)
total_load = 85.5
print('Current Load: ' + str(total_load))

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))
node_1 = "DGX-Cluster-A"
node_2 = "HGX-Cluster-B"

# Python checks the alphabet. 'D' comes before 'H', so DGX is "Less Than" HGX.
if node_1 < node_2:
    print(node_1 + " is prioritized before " + node_2 + " in the deployment sequence.")

user_clearance = "Admin"
required_clearance = "admin"

# Python is case-sensitive! "Admin" does not equal "admin"
if user_clearance == required_clearance:
    print("ACCESS GRANTED: Entering Sovereign Fabric.")
else:
    print("❌ ACCESS DENIED: Case-sensitive mismatch detected.")


number = 10

if number > 11:
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)

def greater_value(x, y):
    if x > y:
        return x
    else:
        return y

print(greater_value(10,3*5))


test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)

def difference(x,y):
    z = x -y
    return z

print(difference(5,3))
print("5" + "5")
