from collections import defaultdict
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        result = 0
        start = 0

        for gr in g:

            while start < len(s):
                if gr <= s[start]:
                    result += 1
                    start += 1
                    break
                start += 1

        return result


