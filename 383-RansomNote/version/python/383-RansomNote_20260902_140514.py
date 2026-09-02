# Last updated: 9/2/2026, 2:05:14 PM
1class Solution:
2    def canConstruct(self, ransomNote, magazine):
3        for char in set(ransomNote):
4            if ransomNote.count(char) > magazine.count(char):
5                return False
6
7        return True