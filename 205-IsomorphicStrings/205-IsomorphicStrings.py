# Last updated: 9/2/2026, 12:40:41 PM
class Solution:
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))