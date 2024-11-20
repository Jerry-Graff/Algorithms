import math


def jump_search(arr, target):
    '''
    """
    Performs Jump Search on a sorted array to find the target value.

    Args:
        arr (list[int]): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int or None: The index of the target if found, otherwise None.

    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    '''

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    count_steps = 0

    while prev < n and arr[min(step, n) - 1] < target:
        count_steps += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return (None, count_steps)

    for i in range(prev, min(step, n)):
        count_steps += 1
        if arr[i] == target:
            return (i, count_steps)

    return (None, count_steps)


# Example Usage:
if __name__ == "__main__":
    # Example 1
    array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index, steps = jump_search(array_1, 9)
    print(f"Index of 9: {index}, Steps taken: {steps}")

    # Example 2
    array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index, steps = jump_search(array_2, 5)
    print(f"Index of 5: {index}, Steps taken: {steps}")

    # Example 3
    array_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index, steps = jump_search(array_3, 14)
    print(f"Index of 14: {index}, Steps taken: {steps}")
