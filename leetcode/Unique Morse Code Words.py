from collections import defaultdict


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        dic = defaultdict(int)

        for word in words:
            w = ""
            for c in word:
                idx = ord(c) - 97
                w += code[idx]
            dic[w] += 1

        result = 0

        for v in dic.values():
            result += 1

        return result