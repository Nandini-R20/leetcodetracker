# Last updated: 9/2/2026, 12:43:42 PM
class Solution:
    def simplifyPath(self, path):
        stack = []

        for part in path.split('/'):
            if part == "" or part == ".":
                continue

            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)