# Last updated: 9/2/2026, 12:41:29 PM
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        first = head
        second = previous

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2