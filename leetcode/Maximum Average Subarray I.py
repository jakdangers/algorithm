class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])

        maxium = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]

            maxium = max(total, maxium)

        return maxium / k