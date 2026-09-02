# Last updated: 9/2/2026, 11:44:21 AM
1class Solution:
2    def isValid(self, s):
3        stack = []
4        pairs = {
5            ')': '(',
6            ']': '[',
7            '}': '{'
8        }
9
10        for ch in s:
11            if ch in pairs:
12                if not stack or stack.pop() != pairs[ch]:
13                    return False
14            else:
15                stack.append(ch)
16
17        return not stack