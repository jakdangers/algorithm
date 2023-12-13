from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s_dict = defaultdict(int)

        answer = 0
        for s in stones:
            s_dict[s] += 1

        for j in jewels:
            answer += s_dict[j]

        return answer
