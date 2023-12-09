class Solution:
    def countElements(self, arr: List[int]) -> int:

        dic = {}

        for e in arr:
            if e not in dic:
                dic[e] = True

        count = 0

        for e in arr:
            if e + 1 in dic:
                count += 1

        return count