# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        counter = 1
        current = head
        prev = None
        first_even = None
        while current!=None and current.next!=None:

            if counter%2==0:
                if first_even==None:
                    first_even=current
                next_one = current.next.next
                prev.next=current.next
                current.next.next = first_even
                current.next = next_one
                prev=prev.next
                current=next_one
                counter+=2

            else:
                counter+=1
                prev = current
                current = current.next
        return head