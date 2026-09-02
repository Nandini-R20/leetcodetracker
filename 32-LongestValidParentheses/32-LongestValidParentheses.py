# Last updated: 9/2/2026, 12:45:23 PM
class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        answer = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    answer = max(answer, i - stack[-1])

        return answer