# Last updated: 11/24/2025, 10:52:16 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     #Most efficient way is makking the hashmap
     prevMap = {}

     for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i
     return 