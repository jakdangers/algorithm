class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)
        curr = 0

        while curr + 1 < n and arr[curr] < arr[curr + 1]:
            curr += 1

        if curr == 0 or curr == n - 1:
            return False

        while curr + 1 < n and arr[curr] > arr[curr + 1]:
            curr += 1

        if curr != n - 1:
            return False

        return True





