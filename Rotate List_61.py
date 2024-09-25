# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None


        counter = 0

        t = head
        while t!=None:
            counter+=1
            t=t.next
        k = k%counter
        if k==0:
            return head
        current = head
        counter = 1
        backward = None

        while current.next!=None:
            if counter==k:
                backward=head
            if counter>k:
                backward=backward.next
            counter += 1
            current=current.next
        if backward==None:
            return head
        else:
            tmp = head
            head = backward.next
            current.next = tmp
            backward.next = None
            return head
