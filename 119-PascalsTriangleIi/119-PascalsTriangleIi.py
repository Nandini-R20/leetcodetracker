# Last updated: 9/2/2026, 12:42:07 PM
class Solution:
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            row.append(0)

            for j in range(i + 1, 0, -1):
                row[j] += row[j - 1]

        return row