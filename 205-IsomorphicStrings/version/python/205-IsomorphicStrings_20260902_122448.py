# Last updated: 9/2/2026, 12:24:48 PM
1class Solution:
2    def reverseList(self, head):
3        prev = None
4        current = head
5
6        while current:
7            next_node = current.next
8            current.next = prev
9            prev = current
10            current = next_node
11
12        return prev