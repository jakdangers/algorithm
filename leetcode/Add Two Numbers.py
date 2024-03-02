# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        head.val = l1.val + l2.val
        increase = False
        l1 = l1.next
        l2 = l2.next

        if head.val > 9:
            head.val = head.val % 10
            increase = True

        dummy = head
        while l1 != None or l2 != None:
            nextNode = ListNode()
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            if increase:
                value += 1
                increase = False

            if value > 9:
                nextNode.val = value % 10
                increase = True
            else:
                nextNode.val = value

            dummy.next = nextNode
            dummy = nextNode

        if increase:
            node = ListNode()
            node.val = 1
            dummy.next = node

        return head
