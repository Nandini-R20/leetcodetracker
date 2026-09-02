# Last updated: 9/2/2026, 12:43:34 PM
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        required = len(need)

        left = 0
        result = ""
        result_len = float('inf')

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if right - left + 1 < result_len:
                    result = s[left:right + 1]
                    result_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return result