# Last updated: 9/2/2026, 12:40:15 PM
class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return

            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

        dfs(root, "")
        return result