# Last updated: 12/12/2025, 1:24:19 PM
1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        # Split s into words
4        words = s.split(" ")
5
6        # If lengths differ, we can't have a 1-to-1 mapping
7        if len(pattern) != len(words):
8            return False
9
10        # charToWord: pattern char -> word
11        # wordToChar: word -> pattern char
12        charToWord = {}
13        wordToChar = {}
14
15        for c, w in zip(pattern, words):
16            # If we've seen c before, it must map to the same word w
17            if c in charToWord and charToWord[c] != w:
18                return False
19
20            # If we've seen w before, it must map to the same char c
21            if w in wordToChar and wordToChar[w] != c:
22                return False
23
24            # Record the mapping in both directions
25            charToWord[c] = w
26            wordToChar[w] = c
27
28        return True
29