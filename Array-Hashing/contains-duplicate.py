from typing import List

"""
Solution 1: HashSet
Time: O(n)
Space: O(n)
Idea: Use a set to store values in the array we have seen, as soon as a value in our set appears again we catch it and return true.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False