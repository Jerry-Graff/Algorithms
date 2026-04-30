"""
Given an integer array nums, return true if any value appears more than
once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""


class SolutionOne:
    """
    Brute force approach that perfomrs O(n2) due to the double loop
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums) + 1):
                if nums[i] == nums[j]:
                    return True

        return False


class SolutionTwo:
    """
    Sort the list first for one iteration with a slidding window O(n log n)
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True

        return False


class SolutionThree:
    """
    Hash set most optimal solution O(n)
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


class SolutionFour:
    """
    One liner hash map
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        return len(set(nums)) < len(nums)

