def two_pointer_search(arr, target):
    '''
    Finds a pair of numbers in a sorted array that sum up to the target value.

    Args:
        arr (list[int]): A sorted list of integers.
        target (int): The target sum to find.

    Returns:
        tuple[int, int] or None: A tuple containing the pair of numbers
        that add up to the target, or None if no such pair exists.

    Time Complexity: O(n)
    Space Complexity: O(1)

    '''
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


# Example 1
array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(two_pointer_search(array_1, 14))  # Expected result: (5, 9)

# Example 2
array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(two_pointer_search(array_2, 7))  # Expected result: (1, 6)

# Example 3
array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(two_pointer_search(array_2, 50))  # Expected result: None


def is_palindrome(word):
    '''
    Checks if a given string is a palindrome, ignoring non-alphanumeric
    characters and case.

    Args:
        word (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n)
    Space Complexity: O(1)

    '''
    left = 0
    right = len(word) - 1

    while left < right:

        while left < right and not word[left].isalnum():
            left += 1
        while left < right and not word[right].isalnum():
            right -= 1

        if word[left].lower() != word[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Examples
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected result: True
print(is_palindrome("sator"))  # Expected result: True
print(is_palindrome("antiestablistmentarianism"))  # Expected result:False
