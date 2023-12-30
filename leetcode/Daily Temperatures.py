class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):

            if stack:
                while stack and temperatures[stack[-1]] < v:
                    idx = stack.pop()
                    result[idx] = i - idx

            stack.append(i)

        return result