class Solution:
    def removeDuplicates(self, s: str) -> str:

        b = []

        for c in s:
            if not b:
                b.append(c)
            elif b[-1] == c:
                b.pop()
            else:
                b.append(c)

        return "".join(b)
