# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表遍历
        def linklist_visit(l: ListNode):
            numstr = ""
            while l:
                numstr += str(l.val)
                l = l.next
            return numstr

        # 数字翻转
        def num_reverse(numstr):
            n = len(numstr)
            s = ""
            for i in range(n-1, -1, -1):
                s += numstr[i]
            print(s)
            return s
        # 构造链表
        def initlinklist(numstr):
            ret = head = ListNode()
            head.val(int(numstr[-1]))
            n = len(str)
            s = ""
            for i in range(n-2, -1, -1):
                net = ListNode()
                net.val = int(numstr[i])
                head.next = net
                head = net
            return ret

        numstr1 = linklist_visit(l1)
        numstr2 = linklist_visit(l2)
        num1 = int(num_reverse(numstr1))
        num2 = int(num_reverse(numstr2))

        return initlinklist(str(num1+num2))