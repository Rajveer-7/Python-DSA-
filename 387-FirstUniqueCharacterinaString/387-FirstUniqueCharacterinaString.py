# Last updated: 12/12/2025, 11:43:22 AM
1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        # Map the character to its count 
4        #L-> 1, e->3, t->1 , - Hashmap , iterate over string  O(n) , then we return the index of the character 
5        #We make a Hashmap ,
6
7        count = defaultdict(int) # char -> count
8
9        for c in s:
10            count[c] += 1
11
12        for i,c in enumerate(s):
13            if count[c] ==1:
14                return i
15        return -1