"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        queue = deque([root])

        while queue:
            count = len(queue)
            arr = []

            for _ in range(count):
                node = queue.popleft()

                arr.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for idx in range(1, len(arr)):
                arr[idx - 1].next = arr[idx]

            arr[-1].next = None

        return root


