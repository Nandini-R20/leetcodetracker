# Last updated: 9/2/2026, 12:43:14 PM
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            duplicate = False

            while current.next and current.val == current.next.val:
                current = current.next
                duplicate = True

            if duplicate:
                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return dummy.next