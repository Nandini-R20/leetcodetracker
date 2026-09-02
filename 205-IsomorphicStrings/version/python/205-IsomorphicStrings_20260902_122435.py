# Last updated: 9/2/2026, 12:24:35 PM
1class Solution:
2    def isIsomorphic(self, s, t):
3        return len(set(zip(s, t))) == len(set(s)) == len(set(t))