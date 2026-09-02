# Last updated: 9/2/2026, 12:43:52 PM
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            while (
                i < len(words)
                and length + len(words[i]) + len(line) <= maxWidth
            ):
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length

            if i == len(words) or len(line) == 1:
                text = " ".join(line)
                text += " " * (maxWidth - len(text))
            else:
                gaps = len(line) - 1
                extra = spaces // gaps
                remainder = spaces % gaps

                text = ""

                for j in range(gaps):
                    text += line[j]
                    text += " " * (extra + (1 if j < remainder else 0))

                text += line[-1]

            result.append(text)

        return result