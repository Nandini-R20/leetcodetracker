# Last updated: 8/11/2026, 12:22:45 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return' '.join(s.split()[::-1])[::-1]