# Last updated: 9/2/2026, 12:40:45 PM
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next