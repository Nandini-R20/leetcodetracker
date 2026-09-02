# Last updated: 9/2/2026, 11:42:28 AM
1class Solution:
2    def romanToInt(self, s):
3        values = {
4            'I': 1,
5            'V': 5,
6            'X': 10,
7            'L': 50,
8            'C': 100,
9            'D': 500,
10            'M': 1000
11        }
12
13        result = 0
14
15        for i in range(len(s)):
16            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
17                result -= values[s[i]]
18            else:
19                result += values[s[i]]
20
21        return result