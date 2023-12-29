class Solution:
    def makeGood(self, s: str) -> str:

        if len(s) < 2:
            return s

        stack = []

        for c in s:

            if stack:
                if stack[-1] == stack[-1].lower() and c.upper() == c and stack[-1].lower() == c.lower():
                    stack.pop()
                    continue

                if stack[-1] == stack[-1].upper() and c.lower() == c and stack[-1].lower() == c.lower():
                    stack.pop()
                    continue

                stack.append(c)

            else:
                stack.append(c)

        return "".join(stack)
