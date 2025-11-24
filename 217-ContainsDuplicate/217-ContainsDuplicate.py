# Last updated: 11/24/2025, 11:06:16 AM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        ans =[]
        for n in nums1:
            hmap[n] = hmap.get(n,0) + 1
        
        for n in nums2:
            if n in hmap and hmap[n] > 0:
                hmap[n]-=1
                ans.append(n)

        return ans