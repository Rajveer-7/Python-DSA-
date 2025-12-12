# Last updated: 12/12/2025, 1:23:07 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        # if words or chars are more , we return false 
4
5        # we make 2 hashmaps 
6        words = s.split(" ")
7        if len(pattern) != len(words):
8            return False
9
10        charToWord = {}
11        wordToChar = {}
12
13        for c, w in zip(pattern, words):
14            if c in charToWord and charToWord[c] != w :
15                return False
16            if w in wordToChar and wordToChar[w] != c:
17                return False 
18
19            charToWord[c] = w
20            wordToChar[w] = c
21        
22        return True