# Last updated: 9/2/2026, 12:43:55 PM
class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return (
                'e' in s.lower()
                or '.' in s
                or s.lstrip('+-').isdigit()
            )
        except:
            return False