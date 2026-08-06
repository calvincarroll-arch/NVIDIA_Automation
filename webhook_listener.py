from flask import Flask, request
import subprocess

# 1. We create our listening robot (the app)
app = Flask(__name__)

# 2. We give the robot an ear (a specific URL path to listen to)
@app.route('/netbox-update', methods=['POST'])
def handle_netbox_change():
    # 3. When NetBox sends a message here, the robot wakes up!
    print("\n🚨 BEEP BEEP: NetBox just detected a change in the Source of Truth!")
    print("🤖 Waking up Nornir to push the new intent to the fabric...\n")
    
    # 4. The robot automatically types the command you used to type manually
    subprocess.run(["python3", "push_roce_config.py"])
    
    # 5. The robot tells NetBox "Got it, mission accomplished."
    return "Configuration pushed successfully!", 200

if __name__ == '__main__':
    # 6. We turn the robot on and tell it to listen on port 5000
    print("🎧 Iron Logic Webhook Listener is online. Waiting for NetBox...")
    app.run(host='0.0.0.0', port=5000)