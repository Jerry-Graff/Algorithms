def two_sum(nums, target):
    """
    Given an array of ints and an int target, return indices of two
    numbers that add up to the target.
    """
    nums_seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in nums_seen:
            return [nums_seen[complement], idx]
        nums_seen[num] = idx
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
