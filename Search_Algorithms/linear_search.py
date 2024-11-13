def linear_search(target, list):
    """
    Simple but powerful, linear search iterates over each element in a
    list and returns the index of the target if found, otherwise None.

    Args:
        target: The value to search for in the list.
        list: A list of elements to search within.

    Returns:
        The index of the target in the list if found; otherwise, None.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    for i in range(len(list)):
        if list[i] == target:
            return i


# Example 1
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(5, list_1))  # Expected result: 4

# Example 2
list_2 = [568, 437, 999, 1001, 57, 33]
print(linear_search(57, list_2))  # Expected result: 4

# Example 3
list_3 = [1, 2, 3, 4, 5]
print(linear_search(10, list_3))  # Expected result: None
