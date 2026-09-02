# Last updated: 9/2/2026, 2:07:02 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        if len(s) > len(t):return False
4        if len(s) == 0:return True
5        subsequence=0
6        for i in range(0,len(t)):
7            if subsequence <= len(s) -1:
8                print(s[subsequence])
9                if s[subsequence]==t[i]:
10
11                    subsequence+=1
12        return  subsequence == len(s) 