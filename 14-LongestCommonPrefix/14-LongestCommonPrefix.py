# Last updated: 9/2/2026, 12:45:54 PM
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix