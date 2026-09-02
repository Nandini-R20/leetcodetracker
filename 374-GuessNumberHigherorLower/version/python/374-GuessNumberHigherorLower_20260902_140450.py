# Last updated: 9/2/2026, 2:04:50 PM
1class Solution:
2    def guessNumber(self, n):
3        left = 1
4        right = n
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            result = guess(mid)
10
11            if result == 0:
12                return mid
13            elif result < 0:
14                right = mid - 1
15            else:
16                left = mid + 1