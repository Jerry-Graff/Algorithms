def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.

    Args:
        arr (list): The list of elements to sort.

    Returns:
        list: A new sorted list containing the same elements as arr.

    Time Complexity: Avergage: O(n log n)
                     Worst: O(n2) e.g. already sorted list, poor pivot - rare
    Space Complexity: O(log n)
    """

    if len(arr) <= 1:
        return arr  # Base Case: 0 or 1 is already sorted

    # Select pivot point
    pivot = arr[-1]
    left = []  # Less than pivot
    right = []  # More than pivot

    for element in arr[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    # Recurive call
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = quick_sort(unsorted_list)
    print(f"Quick Sort Result: {sorted_list}")


"""
    N.B. General note on pivot points:
    1. The median of three rule is a good approach to ensure optimal partitions
       with minimal over head.
    2. If the array is near sorted dont select index 0 or -1 as will lead to
       unbalanced partitions and poor performance.
    3. A good pivot splits the array into two roughly equal halves, leading to
       logarithmic recursion depth and O(n log n) time complexity.

"""


def quick_sort_median_of_three(arr):
    if len(arr) <= 1:
        return arr

    # Median-of-three pivot selection
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    pivot = sorted([first, middle, last])[1]  # Choose median of first, middle, and last

    # List comprehension for partitioning
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    # Count duplicates equal to pivot separately if needed
    return quick_sort(left) + [pivot] * arr.count(pivot) + quick_sort(right)
