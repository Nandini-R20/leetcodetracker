# Last updated: 9/2/2026, 11:52:50 AM
1class Solution:
2    def trap(self, height):
3        left = 0
4        right = len(height) - 1
5
6        left_max = 0
7        right_max = 0
8
9        answer = 0
10
11        while left < right:
12            if height[left] <= height[right]:
13                if height[left] >= left_max:
14                    left_max = height[left]
15                else:
16                    answer += left_max - height[left]
17
18                left += 1
19
20            else:
21                if height[right] >= right_max:
22                    right_max = height[right]
23                else:
24                    answer += right_max - height[right]
25
26                right -= 1
27
28        return answer