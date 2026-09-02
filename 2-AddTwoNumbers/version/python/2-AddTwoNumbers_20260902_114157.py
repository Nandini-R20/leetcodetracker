# Last updated: 9/2/2026, 11:41:57 AM
1class Solution:
2    def maxArea(self, height):
3        left = 0
4        right = len(height) - 1
5        answer = 0
6
7        while left < right:
8            width = right - left
9            area = width * min(height[left], height[right])
10
11            answer = max(answer, area)
12
13            if height[left] < height[right]:
14                left += 1
15            else:
16                right -= 1
17
18        return answer