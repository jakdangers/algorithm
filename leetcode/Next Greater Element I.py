class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        dic = {}

        for num in nums2:
            while stack and stack[-1] < num:
                before = stack.pop()
                dic[before] = num
            stack.append(num)

        result = []
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            else:
                result.append(-1)

        return result

