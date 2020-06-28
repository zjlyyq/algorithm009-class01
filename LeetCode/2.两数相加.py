# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        head.val = l1.val + l2.val
        l1, l2 = l1.next, l2.next
        while l1 or l2:
            num = 0
            if l1:
                num += l1.val
            if l2:
                num += l2.val
            nex = ListNode()
            nex.val = num
            head.next = nex
            head = nex
        return head
