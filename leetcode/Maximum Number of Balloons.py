from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        counts = defaultdict(int)
        answer = float("inf")

        for c in text:
            counts[c] += 1

        for c in "balloon":
            if c == "l" or c == "o":
                answer = min(answer, counts[c] // 2)
            answer = min(counts[c], answer)

        return answer