import re

def rearrange_name(name):
    # Step 1: Deploy the Grabber Claws
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    
    # Step 2: The Safety Net (Iron Logic Upgrade)
    if result is None:
        return name
        
    # Step 3: The Flip
    return "{} {}".format(result[2], result[1])
