class Solution:
    def largestOddNumber(self, num: str) -> str:

        n = len(num)
        last = 0
        is_even = True

        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                last = i
                is_even = False
                break

        if is_even:
            return ""

        return num[:last + 1]