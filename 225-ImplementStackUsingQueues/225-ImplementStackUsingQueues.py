# Last updated: 9/2/2026, 12:40:33 PM
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self):
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        x = self.q[0]
        self.q.append(self.q.popleft())

        return x

    def empty(self):
        return len(self.q) == 0