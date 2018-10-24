# data = array

def rec_binary_search(data, target, low, high):

    # Return True if target is found in indicated portion of a Python list.
    # The search only considers the portion from data[low] to data[high] inclusive.

    if low > high:
        return False               # interval is empty, no match
    else:
        mid = (low + high)//2      # // - Получение целой части от деления
        if target == data[mid]:
            return True            # founde a match
        elif target < data[mid]:
            # recur on the portion left of the middle
            return rec_binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right on the middle
            return rec_binary_search(data, target, mid + 1, high)

# Test array
data = [3, 5, 8, 12, 15, 23, 35, 50]
target = int(input())

# Function call
result = rec_binary_search(data, target, 0, len(data) - 1)

if result == True:
    print("Element is present in array")
else:
    print("Element is not present in array")
