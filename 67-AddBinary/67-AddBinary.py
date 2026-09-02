# Last updated: 9/2/2026, 12:43:53 PM
class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]