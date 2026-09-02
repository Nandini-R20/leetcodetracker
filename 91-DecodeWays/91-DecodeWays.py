# Last updated: 9/2/2026, 12:42:57 PM
class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != '0':
                current += prev1

            two = int(s[i - 1:i + 1])

            if 10 <= two <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1