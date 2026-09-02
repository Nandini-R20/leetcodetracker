# Last updated: 9/2/2026, 12:42:28 PM
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        index = {value: i for i, value in enumerate(inorder)}

        def build(pl, pr, il, ir):
            if pl > pr:
                return None

            root_val = preorder[pl]
            root = TreeNode(root_val)

            mid = index[root_val]
            left_size = mid - il

            root.left = build(
                pl + 1,
                pl + left_size,
                il,
                mid - 1
            )

            root.right = build(
                pl + left_size + 1,
                pr,
                mid + 1,
                ir
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)