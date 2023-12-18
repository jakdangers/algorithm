from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        counter = defaultdict(int)
        dic = defaultdict(str)

        for i in range(len(s)):

            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if counter[t[i]] == 1:
                    return False
                dic[s[i]] = t[i]
                counter[t[i]] += 1

        return True






