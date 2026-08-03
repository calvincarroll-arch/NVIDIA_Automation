import requests
import json

# 1. The API Endpoint (The back window for your specific repo)
url = "https://api.github.com/repos/calvincarroll-arch/NVIDIA_Automation"

# 2. The API Call (The Python robot walking up and asking for the menu)
print(f"Sending GET request to: {url}...\n")
response = requests.get(url)

# 3. The Status Code (The immediate signal from the server)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Success! The server understood the request.\n")
    
    # 4. Parsing the JSON (Reading the structured paper slip)
    # The .json() method instantly converts the text into a Python dictionary
    repo_data = response.json()
    
    # 5. Extracting exactly what we care about from the massive data block
    print("--- IRON LOGIC REPOSITORY DATA ---")
    print(f"Repository Name: {repo_data.get('name')}")
    print(f"Description:     {repo_data.get('description')}")
    print(f"Primary Tech:    {repo_data.get('language')}")
    print(f"Visibility:      {repo_data.get('visibility')}")
    print("----------------------------------")
    
else:
    print("Something went wrong. Did we hit the right endpoint?")
    