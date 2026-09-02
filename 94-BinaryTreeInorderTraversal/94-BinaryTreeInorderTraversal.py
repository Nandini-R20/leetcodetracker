# Last updated: 9/2/2026, 12:42:53 PM
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result