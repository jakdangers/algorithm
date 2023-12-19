from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
            if len(num_set) > k:
                num_set.remove(nums[i - k])
        return False