# Last updated: 9/2/2026, 2:05:58 PM
1class Solution:
2    def firstUniqChar(self, s):
3        for i in range(len(s)):
4            if s.count(s[i]) == 1:
5                return i
6
7        return -1