# Last updated: 9/2/2026, 12:35:41 PM
1class Solution:
2    def reverseVowels(self, s):
3        vowels = set("aeiouAEIOU")
4        s = list(s)
5
6        left = 0
7        right = len(s) - 1
8
9        while left < right:
10            while left < right and s[left] not in vowels:
11                left += 1
12
13            while left < right and s[right] not in vowels:
14                right -= 1
15
16            s[left], s[right] = s[right], s[left]
17
18            left += 1
19            right -= 1
20
21        return "".join(s)