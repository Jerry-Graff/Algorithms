"""
Given two strings s and t, return true if the two strings are anagrams of each 
other, otherwise return false. An anagram is a string that contains the exact 
same characters as another string, but the order of the characters can be 
different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""


class SolutionOne:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):  # If not same len would not be anagram
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True


class SolutionTwo:
    """
    If anagram they would be identical so sort both strings and compare
    """
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
