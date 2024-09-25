# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        pointer_current = head
        pointer_late = None
        counter = 1
        while pointer_current.next!=None:
            if(counter==n):
                pointer_late = head
                pointer_current = pointer_current.next
                counter += 1
            elif counter<n:
                pointer_current=pointer_current.next
                counter+=1
            else:
                pointer_current=pointer_current.next
                counter+=1
                pointer_late = pointer_late.next

        if pointer_late==None:
            pointer_late=head
            head=head.next
            pointer_late.next=None
        else:
            next_pointer = pointer_late.next
            pointer_late.next=next_pointer.next
            next_pointer.next=None
        return head