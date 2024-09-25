# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        prev_start = None
        counter = 1
        prev = None
        ending = None
        next_one = None
        prev_before = None

        current = head
        while current!=None:
            next_current = current.next
            if counter==left:
                prev_before = prev
                prev_start=current
            if counter>left and counter<right:
                current.next=prev
            if counter == right:
                ending = current
                next_one = current.next
                current.next=prev
                prev_start.next = next_one
                if prev_before!=None:
                    prev_before.next=current
                else:
                    head=current
                break


            prev=current
            current=next_current
            counter+=1
        return head