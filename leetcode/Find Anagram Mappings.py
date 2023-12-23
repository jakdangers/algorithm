class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dic = {}

        for i in range(len(nums2)):
            if nums2[i] not in dic:
                dic[nums2[i]] = i

        result = []

        for n in nums1:
            result.append(dic[n])

        return result