# Last updated: 9/2/2026, 12:28:01 PM
1from collections import deque
2
3class MyStack:
4
5    def __init__(self):
6        self.q = deque()
7
8    def push(self, x):
9        self.q.append(x)
10
11    def pop(self):
12        for _ in range(len(self.q) - 1):
13            self.q.append(self.q.popleft())
14
15        return self.q.popleft()
16
17    def top(self):
18        for _ in range(len(self.q) - 1):
19            self.q.append(self.q.popleft())
20
21        x = self.q[0]
22        self.q.append(self.q.popleft())
23
24        return x
25
26    def empty(self):
27        return len(self.q) == 0