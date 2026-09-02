# Last updated: 9/2/2026, 12:41:23 PM
class Solution:
    def convertToTitle(self, columnNumber):
        result = ""
        
        while columnNumber:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        
        return result