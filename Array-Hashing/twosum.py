"""
Solution
Time: O(n)
Space: O(n)
Idea: Find the complement of current and see if we have seen it in the hashmap. If yes then return it.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i, num in enumerate(nums):

            complement  = target - num

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[num] = i

"""
Alt Solution
Time: O(n^2)
Space: O(1)
Idea: Not coding because this is a bad appraoch but just iterate over remainder of array for each value in array and see if they add up to the target.
"""