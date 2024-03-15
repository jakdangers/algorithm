class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0
        stack = [prices[0]]

        for p in prices[1:]:
            if stack[-1] > p:
                stack.pop()
                stack.append(p)
            else:
                curr = p - stack[-1]
                max_price = max(max_price, curr)

        return max_price