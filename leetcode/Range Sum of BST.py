# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total = 0

        def find(node):
            nonlocal total

            if not node:
                return 0

            if low <= node.val and high >= node.val:
                total += node.val

            if node.val > low and node.left:
                find(node.left)

            if node.val <= high and node.right:
                find(node.right)

        find(root)

        return total

