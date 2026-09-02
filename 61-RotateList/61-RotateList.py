# Last updated: 9/2/2026, 12:44:07 PM
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        current = head
        length = 1

        while current.next:
            current = current.next
            length += 1

        k %= length

        if k == 0:
            return head

        current.next = head

        steps = length - k

        for _ in range(steps):
            current = current.next

        new_head = current.next
        current.next = None

        return new_head