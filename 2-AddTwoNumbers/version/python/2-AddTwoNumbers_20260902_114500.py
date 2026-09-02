# Last updated: 9/2/2026, 11:45:00 AM
1import heapq
2
3class Solution:
4    def mergeKLists(self, lists):
5        heap = []
6
7        for i, node in enumerate(lists):
8            if node:
9                heapq.heappush(heap, (node.val, i, node))
10
11        dummy = ListNode(0)
12        current = dummy
13
14        while heap:
15            value, i, node = heapq.heappop(heap)
16
17            current.next = node
18            current = current.next
19
20            if node.next:
21                heapq.heappush(
22                    heap,
23                    (node.next.val, i, node.next)
24                )
25
26        return dummy.next