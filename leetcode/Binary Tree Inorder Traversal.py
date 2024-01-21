# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = []
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                res.append(node.val)
                curr = node.right

        return res

