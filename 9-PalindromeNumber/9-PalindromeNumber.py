# Last updated: 9/2/2026, 12:46:04 PM
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        return str(x) == str(x)[::-1]