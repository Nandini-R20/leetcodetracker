# Last updated: 9/2/2026, 12:42:09 PM
from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = deque([root])

        while queue:
            previous = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if previous:
                    previous.next = node

                previous = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            previous.next = None

        return root