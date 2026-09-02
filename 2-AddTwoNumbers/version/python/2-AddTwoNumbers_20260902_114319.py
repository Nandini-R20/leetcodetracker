# Last updated: 9/2/2026, 11:43:19 AM
1class Solution:
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4
5        answer = nums[0] + nums[1] + nums[2]
6
7        for i in range(len(nums) - 2):
8            left = i + 1
9            right = len(nums) - 1
10
11            while left < right:
12                total = nums[i] + nums[left] + nums[right]
13
14                if abs(total - target) < abs(answer - target):
15                    answer = total
16
17                if total < target:
18                    left += 1
19                elif total > target:
20                    right -= 1
21                else:
22                    return total
23
24        return answer