# Last updated: 9/2/2026, 11:41:16 AM
1class Solution:
2    def isPalindrome(self, x):
3        if x < 0:
4            return False
5
6        return str(x) == str(x)[::-1]