# Last updated: 9/2/2026, 12:40:13 PM
class Solution:
    def addDigits(self, num):
        while num >= 10:
            total = 0

            while num:
                total += num % 10
                num //= 10

            num = total

        return num