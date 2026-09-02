# Last updated: 9/2/2026, 12:45:22 PM
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        need = Counter(words)
        result = []

        for start in range(word_len):
            left = start
            count = 0
            window = Counter()

            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    window[word] += 1
                    count += 1

                    while window[word] > need[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return result