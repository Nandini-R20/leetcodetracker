# Last updated: 9/2/2026, 12:33:02 PM
1class Solution:
2    def wordPattern(self, pattern, s):
3        words = s.split()
4
5        if len(pattern) != len(words):
6            return False
7
8        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))