# Last updated: 9/2/2026, 12:40:17 PM
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)