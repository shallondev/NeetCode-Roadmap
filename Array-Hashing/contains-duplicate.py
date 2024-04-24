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

"""
Solution 2: Sorting
Time: O(nlogn) - sorting a array takes nlogn time (think merge sort)
Space: O(1)
Idea: sort the array then check two values at a time if they are the same return True.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        
        return False