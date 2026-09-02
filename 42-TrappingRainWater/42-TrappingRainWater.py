# Last updated: 9/2/2026, 12:44:56 PM
class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        answer = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    answer += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    answer += right_max - height[right]

                right -= 1

        return answer