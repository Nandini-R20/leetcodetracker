# Last updated: 9/2/2026, 12:46:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            answer = max(answer, right - left + 1)

        return answer