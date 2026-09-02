# Last updated: 9/2/2026, 11:54:06 AM
1class Solution:
2    def jump(self, nums):
3        jumps = 0
4        current_end = 0
5        farthest = 0
6
7        for i in range(len(nums) - 1):
8            farthest = max(farthest, i + nums[i])
9
10            if i == current_end:
11                jumps += 1
12                current_end = farthest
13
14        return jumps