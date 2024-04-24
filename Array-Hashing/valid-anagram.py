"""
Solution 1: Counter/Hashmap
Time: O(max(n,m)) - create counters
Space: O(n + m) - two counters
Idea: Create two counter objects that operate like hashmaps storing the occurances of each letter. Then see if the counters are equal.
"""
from typing import Counter

# Using Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter1 = Counter(s) # O(n) to build a counter
        counter2 = Counter(t)

        if counter1 == counter2:
            return True
        return False
    
# Using hashmap - slight optmization 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If hashmaps length do not match we are done
        if len(s) != len(t):
            return False

        # Declare hashmaps
        countS, countT = {}, {}

        # Build hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Iterate hashmaps and compare
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    
"""
Solution 2: Sorting
Time: O(max(nlogn, mlogm)) - time to sort
Space: O(n + m) - Need to create a sorted array out of the string.
Idea: Sort then see if the strings are equal.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s)) # Takes O(nlogn) time to and create a new array of size O(n)
        t = ''.join(sorted(t))

        if s == t:
            return True
        return False