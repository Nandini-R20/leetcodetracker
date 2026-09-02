# Last updated: 9/2/2026, 11:42:41 AM
1class Solution:
2    def longestCommonPrefix(self, strs):
3        prefix = strs[0]
4
5        for s in strs[1:]:
6            while not s.startswith(prefix):
7                prefix = prefix[:-1]
8
9                if not prefix:
10                    return ""
11
12        return prefix