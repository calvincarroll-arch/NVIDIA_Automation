def find_number(target, numbers):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        
        # DEBUG CHECKPOINT 1
        print(f"DEBUG | Left: {left} | Right: {right} | Middle Index: {middle} | Middle Value: {numbers[middle]}")

        if numbers[middle] == target:
            return f"Found {target} at index {middle}!"
        
        elif numbers[middle] < target:
            left = middle + 1 # 🚨 THE BUG IS HERE! It should be: left = middle + 1
        else:
            right = middle - 1

    return "Number not found."

# Let's hunt for the number 8
my_list = [1, 3, 5, 7, 9, 11]
print(find_number(8, my_list))