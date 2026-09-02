# Last updated: 9/2/2026, 12:42:55 PM
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            temp = current.next

            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next