# Last updated: 9/2/2026, 12:28:13 PM
1class Solution:
2    def invertTree(self, root):
3        if not root:
4            return None
5
6        root.left, root.right = root.right, root.left
7
8        self.invertTree(root.left)
9        self.invertTree(root.right)
10
11        return root