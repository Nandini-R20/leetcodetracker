# Last updated: 8/11/2026, 12:24:54 PM
class Solution:
    def reverseWords(self, s: str) -> str:
       
        return " ".join(s.split()[::-1])