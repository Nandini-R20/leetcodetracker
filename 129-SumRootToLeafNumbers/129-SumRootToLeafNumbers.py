# Last updated: 9/2/2026, 12:41:54 PM
class Solution:
    def sumNumbers(self, root):
        def dfs(node, value):
            if not node:
                return 0

            value = value * 10 + node.val

            if not node.left and not node.right:
                return value

            return dfs(node.left, value) + dfs(node.right, value)

        return dfs(root, 0)