# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node):
            nonlocal arr

            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

            return arr

        dfs(root)

        res = float('inf')
        for idx in range(1, len(arr)):
            res = min(res, arr[idx] - arr[idx - 1])

        return res