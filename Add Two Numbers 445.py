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
        stack_one = []
        stack_two = []

        current = l1
        while current!=None:
            stack_one.append(current.val)
            current=current.next

        current = l2
        while current!=None:
            stack_two.append(current.val)
            current=current.next

        carry = 0
        head = None
        prev = None

        while len(stack_one)>0 or len(stack_two)>0:
            num1=0
            if len(stack_one)>0:
                num1 = stack_one.pop()
            num2=0
            if len(stack_two)>0:
                num2 = stack_two.pop()

            num = num1+num2+carry
            carry = num//10
            node = ListNode()
            node.val=num%10
            if prev==None:
                prev=node
                head=node
            else:
                node.next=prev
                prev=node
                head=node
        if carry>0:
            node = ListNode()
            node.val=carry
            if prev==None:
                prev=node
                head=node
            else:
                node.next=prev
                prev=node
                head=node
        return head
