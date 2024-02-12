class Solution:
    def isPalindrome(self, x: int) -> bool:

        target = list(str(x))
        left = 0
        right = len(target) - 1

        while left < right:
            if target[left] != target[right]:
                return False
            left += 1
            right -= 1

        return True