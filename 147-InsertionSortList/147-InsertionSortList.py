# Last updated: 9/2/2026, 12:41:27 PM
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)

        current = head

        while current:
            previous = dummy

            while previous.next and previous.next.val < current.val:
                previous = previous.next

            next_node = current.next

            current.next = previous.next
            previous.next = current

            current = next_node

        return dummy.next