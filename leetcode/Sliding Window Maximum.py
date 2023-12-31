from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return nums

        de = deque()
        re = []

        for i in range(len(nums)):

            if not de:
                de.append(i)
            else:
                insert = True
                for j in range(len(de)):
                    if nums[de[j]] < nums[i]:
                        de.insert(j, i)
                        insert = False
                        break
                if insert:
                    de.append(i)

            if len(de) == k:
                re.append(nums[de[0]])
                de.remove(i - k + 1)

        return re


