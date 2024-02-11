class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for num in nums:
            positive = abs(num)
            if nums[positive - 1] > 0:
                nums[positive - 1] = -1 * nums[positive - 1]

        result = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                result.append(idx + 1)

        return result