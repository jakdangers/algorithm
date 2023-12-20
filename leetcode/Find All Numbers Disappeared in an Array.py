class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = True

        result = []
        for n in range(1, n + 1):

            if n not in dic:
                result.append(n)

        return result