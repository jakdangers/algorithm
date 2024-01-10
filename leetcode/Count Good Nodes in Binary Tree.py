# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        result = 0
        maxE = float("-inf")
        stack = [(root, maxE)]

        while stack:
            node, e = stack.pop()

            if e <= node.val:
                result += 1
                e = node.val

            if node.left:
                stack.append((node.left, e))
            if node.right:
                stack.append((node.right, e))

        return result