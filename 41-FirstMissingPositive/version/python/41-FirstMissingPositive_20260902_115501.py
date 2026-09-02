# Last updated: 9/2/2026, 11:55:01 AM
1from collections import defaultdict
2
3class Solution:
4    def groupAnagrams(self, strs):
5        groups = defaultdict(list)
6
7        for s in strs:
8            key = ''.join(sorted(s))
9            groups[key].append(s)
10
11        return list(groups.values())