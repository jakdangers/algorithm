from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dic = defaultdict(int)

        degree_arr = []
        max_degree = 0

        for n in nums:
            dic[n] += 1
            if max_degree < dic[n]:
                max_degree = dic[n]

        for k, v in dic.items():
            if v == max_degree:
                degree_arr.append(k)

        result = 50001

        n = len(nums)
        for d in degree_arr:
            start = 0
            end = 0

            for i in range(n):
                if nums[i] == d:
                    start = i
                    break
            for i in range(n - 1, -1, -1):
                if nums[i] == d:
                    end = i
                    break
            result = min(end - start + 1, result)

        return result