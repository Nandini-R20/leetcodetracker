# Last updated: 9/2/2026, 11:48:00 AM
1from collections import Counter
2
3class Solution:
4    def findSubstring(self, s, words):
5        if not s or not words:
6            return []
7
8        word_len = len(words[0])
9        word_count = len(words)
10        total_len = word_len * word_count
11
12        if total_len > len(s):
13            return []
14
15        need = Counter(words)
16        result = []
17
18        for start in range(word_len):
19            left = start
20            count = 0
21            window = Counter()
22
23            for right in range(start, len(s) - word_len + 1, word_len):
24                word = s[right:right + word_len]
25
26                if word in need:
27                    window[word] += 1
28                    count += 1
29
30                    while window[word] > need[word]:
31                        left_word = s[left:left + word_len]
32                        window[left_word] -= 1
33                        left += word_len
34                        count -= 1
35
36                    if count == word_count:
37                        result.append(left)
38
39                        left_word = s[left:left + word_len]
40                        window[left_word] -= 1
41                        left += word_len
42                        count -= 1
43
44                else:
45                    window.clear()
46                    count = 0
47                    left = right + word_len
48
49        return result