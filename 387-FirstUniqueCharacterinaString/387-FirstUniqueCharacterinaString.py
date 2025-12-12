# Last updated: 12/12/2025, 12:13:29 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        #Hashmap - O(n) - iterating through both strings, 
4        mapST, mapTS = {}, {}
5
6        for i in range(len(s)):  # for c1, c2 in zip(s,t)
7            c1, c2 = s[i], t[i]
8
9            if ((c1 in mapST and mapST[c1] != c2) or
10                (c2 in mapTS and mapTS[c2] != c1)):
11                return False
12
13
14            mapST[c1] = c2
15            mapTS[c2] = c1
16        return True