# Last updated: 9/2/2026, 11:44:04 AM
1class Solution:
2    def removeNthFromEnd(self, head, n):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        first = dummy
7        second = dummy
8
9        for _ in range(n + 1):
10            first = first.next
11
12        while first:
13            first = first.next
14            second = second.next
15
16        second.next = second.next.next
17
18        return dummy.next