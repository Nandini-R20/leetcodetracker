# Last updated: 9/2/2026, 12:42:46 PM
class Solution:
    def generateTrees(self, n):

        def build(left, right):
            if left > right:
                return [None]

            result = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        result.append(root)

            return result

        return build(1, n)