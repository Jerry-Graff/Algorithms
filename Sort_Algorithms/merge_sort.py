def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.

    Args:
        arr (list): The list of elements to sort.

    Returns:
        list: A new sorted list containing the same elements as arr.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """

    if len(arr) <= 1:
        return arr  # Base Case: 1 or 0 is already sorted

    # Divide: Split the array into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recurive call left
    right_half = merge_sort(arr[mid:])  # Recursive call right

    # Conquer: Merge the sorted arrays
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Args:
        left (list): A sorted list.
        right (list): A sorted list.

    Returns:
        list: A merged and sorted list containing all elements from left and
        right.
    """

    merged_list = []
    left_idx = right_idx = 0

    # Compare elements from left and right and append the smaller one
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from lefr or right
    while left_idx < len(left):
        merged_list.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        merged_list.append(right[right_idx])
        right_idx += 1

    return merged_list


if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_list)
    print(f"Merge Sort Result: {sorted_list}\n")

    import random
    random_ints_list = [random.randint(1, 100) for _ in range(100)]
    print(f"Unsorted list: {random_ints_list}\n")
    sorted_random_ints = merge_sort(random_ints_list)
    print(f"Sorted list: {sorted_random_ints}")
