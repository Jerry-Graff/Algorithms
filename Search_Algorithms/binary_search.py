def binary_search(target, list):
    """
    Perform binary search on a sorted list to find the target value.

    Args:
        target: The value to search for in the list.
        list: A sorted list of elements to search within.

    Returns:
        A tuple (index, steps):
            - index: The position of the target in the list if found, otherwise None.
            - steps: The number of steps (iterations) taken to find the target.

    Time complexity: 0(logn)
    Space complexity: 0(1)
    """
    low = 0
    high = len(list) - 1
    steps = 0

    while high >= low:
        steps += 1
        mid = (low + high) // 2

        if list[mid] == target:
            return mid, steps
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None, steps


# Example 1
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index, steps = binary_search(5, list_1)
print(f"Target found at index {index} in {steps} steps.")  # Expected output: 4, 1.

# Example 2
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index, steps = binary_search(10, list_1)
print(f"Target found at index {index} in {steps} steps.")  # Expected output: None, 10.

# Example 3
list_1 = [10, 65, 301, 1, 5000, 200, 3, 4, 27]
index, steps = binary_search(3, list_1)
print(f"Target found at index {index} in {steps} steps.")  # Invalid result as list not sorted.
