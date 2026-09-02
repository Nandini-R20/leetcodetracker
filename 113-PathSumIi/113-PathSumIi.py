# Last updated: 9/2/2026, 12:42:12 PM
class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                if remaining == node.val:
                    result.append(path[:])
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            path.pop()

        dfs(root, targetSum, [])

        return result