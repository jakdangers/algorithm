class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        result = []
        count = 0

        for c in s:
            if c == "(":
                count += 1
                if count > 1:
                    result.append(c)
            elif c == ")":
                if count > 1:
                    result.append(c)
                    count -= 1
                else:
                    count -= 1

        return "".join(result)