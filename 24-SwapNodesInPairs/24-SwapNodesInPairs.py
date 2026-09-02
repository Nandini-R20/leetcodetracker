# Last updated: 9/2/2026, 12:45:32 PM
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = first.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next