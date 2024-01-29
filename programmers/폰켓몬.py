from collections import defaultdict
def solution(nums):
    dic = defaultdict(int)
    mx = len(nums) // 2

    for num in nums:
        dic[num] += 1

    gerne = len(list(dic.keys()))

    return min(gerne, mx)