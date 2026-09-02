# Last updated: 9/2/2026, 12:42:37 PM
class Solution:
    def recoverTree(self, root):
        first = None
        second = None
        previous = None

        def inorder(node):
            nonlocal first, second, previous

            if not node:
                return

            inorder(node.left)

            if previous and previous.val > node.val:
                if first is None:
                    first = previous

                second = node

            previous = node

            inorder(node.right)

        inorder(root)

        first.val, second.val = second.val, first.val