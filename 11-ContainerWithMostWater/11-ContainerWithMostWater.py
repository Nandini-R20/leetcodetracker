# Last updated: 9/2/2026, 12:46:01 PM
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        answer = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])

            answer = max(answer, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer