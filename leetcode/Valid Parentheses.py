class Solution:
    def isValid(self, s: str) -> bool:

        se = []

        for b in list(s):
            if b == ")" or b == "}" or b == "]":
                if len(se) == 0:
                    return False
                front = se.pop()
                if b == ")" and front != "(":
                    return False
                if b == "}" and front != "{":
                    return False
                if b == "]" and front != "[":
                    return False
            else:
                se.append(b)

        if se:
            return False

        return True