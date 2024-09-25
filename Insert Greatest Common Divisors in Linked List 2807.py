# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):


    def GCD(self,number1,number2):

        num1=number1
        num2=number2
        while num1!=num2:
            if num1>num2:
                num1-=num2
            else:
                num2-=num1
        return num1

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        prev = None
        while node!=None:
            if prev!=None:
                number = self.GCD(prev.val,node.val)
                new_node = ListNode(number)
                prev.next=new_node
                new_node.next=node

            prev=node
            node=node.next
        return head