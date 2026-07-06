
# # # x = 0
# # # while x < 3:
# # #     x += 1
# # # else:
# # #     print('Done')

# # # z = [x*2 for x in range(4) if x % 2 ==0]
# # # print(z)

# # def get_photo_date(filename):
# #     """Extracts the date from a raw photo filename."""
# #     # This splits "DSC_20260510.raw" and grabs the "20260510" part
# #     extracted_date = filename.split("_")[1].replace(".raw", "")
    
# #     # ❌ FIX ME: Right now, this just shouts from the garage! 
# #     # Change this line so it actually hands the data back to the machine.
# #     return(extracted_date) 


# # # # --- The Main Automation Pipeline ---
# # # if __name__ == "__main__":
# # #     print("[*] Processing new photo...")
# # #     file_target = "DSC_20260510.raw"

# # #     # We try to catch the date in a variable called 'date_folder'
# # #     date_folder = get_photo_date(file_target)

# # #     # Let's see what the machine actually caught:
# # #     print(f"[*] The machine caught: {date_folder}")
    
# # #     # This will look broken right now because date_folder is 'None'
# # #     print(f"[*] Moving {file_target} into folder: /backups/{date_folder}/")

# # # def process_raw(filename):
# # #     """Converts a raw photo file to a compressed jpg format."""
    
# # #     # We invent a new variable INSIDE the treehouse (Local Scope)
# # #     temp_file = filename.replace(".raw", ".jpg")
    
# # #     # We hand the finished data out the window
# # #     return temp_file


# # # # --- The Main Automation Pipeline ---
# # # if __name__ == "__main__":
# # #     print("[*] Starting image compression...")
    
# # #     # We call the function and catch the data in a NEW variable called 'clean_image'
# # #     clean_image = process_raw("sunset.raw")
    
# # #     # ❌ FIX ME: The machine is trying to look inside the closed treehouse!
# # #     # It's trying to print 'temp_file', but that variable is dead.
# # #     # Change this line to print the variable that actually caught the data outside the treehouse.
# # #     print(f"[*] Success. Image processed to: {temp_file}")

# # # def process_raw(filename):
# # #     """Converts a raw photo file to a compressed jpg format."""
    
# # #     # We invent a new variable INSIDE the treehouse (Local Scope)
# # #     temp_file = filename.replace(".raw", ".jpg")
    
# # #     # We hand the finished data out the window
# # #     return temp_file


# # # # --- The Main Automation Pipeline ---
# # # if __name__ == "__main__":
# # #     print("[*] Starting image compression...")
    
# # #     # We call the function and catch the data in a NEW variable called 'clean_image'
# # #     clean_image = process_raw("sunset.raw")
    
# # #     # ❌ FIX ME: The machine is trying to look inside the closed treehouse!
# # #     # It's trying to print 'temp_file', but that variable is dead.
# # #     # Change this line to print the variable that actually caught the data outside the treehouse.


# # # # 🛠️ production/practice_draft_3.py

# # # # We create a 'parameter' bucket called 'image_name'
# # # def rename_and_backup(image_name):
# # #     """Takes a filename, creates a folder, and returns the path."""
    
# # #     # We use the variable passed into our 'bucket'
# # #     print(f"[*] Processing: {image_name}")
    
# # #     # We pretend to do the folder creation logic here
# # #     new_path = f"/backups/processed_{image_name}"
    
# # #     return new_path


# # # # --- The Main Automation Pipeline ---
# # # if __name__ == "__main__":
# # #     # We feed the function the data it needs to work on!
# # #     file_1 = rename_and_backup("beach.raw")
# # #     file_2 = rename_and_backup("mountain.raw")
    
# # #     print(f"[*] Done! Backup 1: {file_1}")
# # #     print(f"[*] Done! Backup 2: {file_2}")

# # # # 🛠️ production/practice_draft_3.py

# # # # We create a 'parameter' bucket called 'image_name'
# # # def rename_and_backup(image_name):
# # #     """Takes a filename, creates a folder, and returns the path."""
    
# # #     # We use the variable passed into our 'bucket'
# # #     print(f"[*] Processing: {image_name}")
    
# # #     # We pretend to do the folder creation logic here
# # #     new_path = f"/backups/processed_{image_name}"
    
# # #     return new_path


# # # # --- The Main Automation Pipeline ---
# # # if __name__ == "__main__":
# # #     # We feed the function the data it needs to work on!
# # #     file_1 = rename_and_backup("beach.raw")
# # #     file_2 = rename_and_backup("mountain.raw")
# # #     file_3 = rename_and_backup("canyon.raw")
    
# # #     print(f"[*] Done! Backup 1: {file_1}")
# # #     print(f"[*] Done! Backup 2: {file_2}")
# # #     print(f"[*] Done! Backup 3: {file_3}")

# # # def rename_and_backup(image_name):
# # #     return f"/backups/processed_{image_name}"

# # # # A list of files we want to process
# # # file_list = ["beach.raw", "mountain.raw", "canyon.raw", "desert.raw", "forest.raw"]

# # # # The Loop: It automatically grabs every file in our list, 
# # # # one by one, and runs the function!
# # # for image in file_list:
# # #     result = rename_and_backup(image)
# # #     print(f"[*] Successfully backed up: {result}")

# # # print("[*] All files processed!")

# # # --- Draft 6: The Log Sanitizer ---
# # # Objective: Take raw messy telemetry strings and output a clean, parsable format.

# # def sanitize_telemetry_log(raw_log):
# #     """
# #     Cleans raw log input:
# #     1. Removes leading/trailing whitespace.
# #     2. Standardizes internal delimiters (e.g., replaces pipes with commas).
# #     3. Extracts the status code hidden at the end of the string.
# #     """
    
# #     # Step 1: Strip extra whitespace
# #     clean_str = raw_log.strip()
    
# #     # Step 2: Standardize delimiter (replace '|' with ',')
# #     standardized = clean_str.replace('|', ',')
    
# #     # Step 3: Isolate status code (assuming it's after the last comma)
# #     parts = standardized.rsplit(',', 1)
    
# #     if len(parts) > 1:
# #         data_body = parts[0]
# #         status_code = parts[1].strip()
# #     else:
# #         data_body = parts[0]
# #         status_code = "UNKNOWN"
        
# #     return {
# #         "body": data_body,
# #         "status": status_code
# #     }

# # # Test execution:
# # raw_input = "  CPU_TEMP|88|MEM_USAGE|45|STAT_CODE_200  "
# # result = sanitize_telemetry_log(raw_input)

# # print(f"Original: '{raw_input}'")
# # print(f"Cleaned Body: {result['body']}")
# # print(f"Status: {result['status']}")

# # telemetry_line = "TEMP,,ID001,23.5,1684567890"

# # def parse_line(line):
# #     # .split(',') breaks the string into a list every time it sees a comma
# #     parts = line.split(',')
    
# #     # We verify the data structure before accessing it to prevent crashes
# #     if len(parts) == 4:
# #         data_type = parts[0].strip()
# #         device_id = parts[1].strip()
# #         value = float(parts[2].strip())
# #         timestamp = int(parts[3].strip())
        
# #         return {
# #             "type": data_type,
# #             "id": device_id,
# #             "value": value,
# #             "time": timestamp
# #         }
# #     else:
# #         print(f"Error: Malformed line: {line}")
# #         return None

# # # Test the function
# # result = parse_line(telemetry_line)
# # if result:
# #     print(f"Successfully parsed: {result}")


# # def parse_log_line(line, delimiter=','):
# #     """
# #     Parses a log line based on a dynamic delimiter.
# #     """
# #     # Use the delimiter argument to make the function flexible
# #     parts = line.split(delimiter)
    
# #     # Defensive programming: Only process if we have the expected number of fields
# #     if len(parts) >= 3: # Allowing flexibility for extra fields
# #         return {
# #             "module": parts[0].strip(),
# #             "timestamp": parts[1].strip(),
# #             "message": parts[2].strip()
# #         }
# #     return None

# # # Test the robust parser
# # log_line = "SYSTEM; 2026-05-27; Boot initiated"

# # # Now we can pass the semicolon as a delimiter
# # result = parse_log_line(log_line, delimiter=';')

# # if result:
# #     print(f"Parsed Log: {result}")
# # else:
# #     print("Failed to parse this line.")
# # The Messy Dough
# text = "NVIDIA-DGX-A100-80GB"

# # We want to break this into pieces every time we see a '-'
# pieces = text.split("-")

# # Let's see what we got!
# print(pieces)

# def parse_log_line(line):
#     """
#     Parses a log line in the format 'DATE-LEVEL-MESSAGE'.
#     Returns the message part, or None if the format is invalid.
#     """
#     # 1. The Safety Net: Check if the line is empty
#     if not line:
#         return None
    
#     # 2. Split the line into a list
#     parts = line.split("-")
    
#     # 3. The Length Guard: Check if the train has at least 3 boxcars
#     if len(parts) < 3:
#         return None
        
#     # Return the message (the third item, index 2)
#     return parts[2]

# # --- Testing the Parser ---
# test_logs = [
#     "2023-INFO-System Started",  # Good
#     "2023-ERROR-Disk Full",      # Good
#     "",                          # Empty line (Should be caught by 'not line')
#     "2023-INFO",                 # Too short (Should be caught by 'len')
# ]

# for log in test_logs:
#     result = parse_log_line(log)
#     if result:
#         print(f"Success: {result}")
#     else:
#         print(f"Skipped invalid line: '{log}'")

# --- EXERCISE 1: Dictionary Access ---
def get_user_age(user_data):
    # PROBLEM: If 'user_data' is an empty dictionary {}, 
    # user_data["age"] will raise a KeyError.
    # ----------------------------------------------------
    if not user_data:
        return None
    
    return user_data["age"]

# --- EXERCISE 2: List Indexing ---
def get_third_item(items):
    # PROBLEM: If the list has fewer than 3 items,
    # items[2] will raise an IndexError.
    # ----------------------------------------------------
    if len(items) < 3:
        return None
    
    return items[2]

# --- EXERCISE 3: Dictionary & Nested Keys ---
def get_user_city(user_data):
    # PROBLEM: If 'user_data' doesn't have an "address" key,
    # user_data["address"]["city"] will crash.
    # ----------------------------------------------------
    if "address" not in user_data:
        return None
    
    return user_data["address"]["city"]

# --- TEST YOUR CODE ---
print(get_user_age({}))                  # Expected: None
print(get_third_item(["a", "b"]))        # Expected: None
print(get_user_city({"name": "Bob"}))    # Expected: None

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(f"\nDictionary: {file_counts}")



















