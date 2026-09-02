# Last updated: 9/2/2026, 12:43:10 PM
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        answer = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = [-1]

            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    answer = max(answer, h * width)

                stack.append(i)

        return answer