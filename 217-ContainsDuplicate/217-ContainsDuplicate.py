# Last updated: 11/21/2025, 3:26:10 AM
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False