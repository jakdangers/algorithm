class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f = float('-inf')
        s = float('-inf')
        t = float('-inf')

        for num in nums:
            if num == f or num == s:
                continue
            if num > f:
                t = s
                s = f
                f = num
            elif num > s:
                t = s
                s = num
            elif num > t:
                t = num

        if t != float('-inf'):
            return t

        return f