# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = None
        prev = None
        elem1 = l1
        elem2 = l2
        transfer = 0
        first = None
        while (elem1 is not None or elem2 is not None):
            number1 = 0
            if(elem1!=None):
                number1 = elem1.val
                elem1 = elem1.next
            number2 = 0
            if(elem2!=None):
                number2 = elem2.val
                elem2 = elem2.next
            sum = number2 + number1 + transfer
            transfer = sum/10
            sum = sum % 10
            res = ListNode(sum,None)
            if first is None:
                first=res
            if(prev is not None):
                prev.next = res
            prev=res

        if (transfer>0):
            res = ListNode(transfer,None)
            if first is None:
                first=res
            if(prev is not None):
                prev.next = res
        return first
