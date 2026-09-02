# Last updated: 9/2/2026, 12:41:34 PM
from functools import lru_cache

class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)

        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for rest in dfs(end):
                        if rest:
                            result.append(word + " " + rest)
                        else:
                            result.append(word)

            return result

        return dfs(0)