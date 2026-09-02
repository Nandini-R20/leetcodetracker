# Last updated: 9/2/2026, 12:43:40 PM
class Solution:
    def minDistance(self, word1, word2):
        n = len(word2)

        dp = list(range(n + 1))

        for i in range(1, len(word1) + 1):
            previous = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                current = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = previous
                else:
                    dp[j] = 1 + min(
                        previous,
                        dp[j],
                        dp[j - 1]
                    )

                previous = current

        return dp[n]