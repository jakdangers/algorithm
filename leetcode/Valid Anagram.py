from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dic = defaultdict(int)
        n = len(s)

        for i in range(n):
            dic[s[i]] += 1
            dic[t[i]] -= 1

        for i, v in dic.items():
            if v != 0:
                return False

        return True
