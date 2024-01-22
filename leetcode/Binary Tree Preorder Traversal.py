# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pre(node, arr):
            if not node:
                return

            arr.append(node.val)
            pre(node.left, arr)
            pre(node.right, arr)

        arrt = []
        pre(root, arrt)

        return arrt

