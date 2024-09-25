# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head==None or head.next==None:
            return head

        current = head
        slow = None
        counter = 1
        prev_slow = None
        first = None
        prev_first = None
        while current!=None:
            if counter==k-1 and k>1:
                prev_first=current
            if counter==k:
                first=current
                slow=head

            current = current.next

            if counter>k:
                prev_slow = slow
                slow=slow.next


            counter+=1

        if prev_first!=None:
            prev_first.next=slow
        else:
            head=slow

        if prev_slow!=None:
            prev_slow.next=first
        else:
            head=first

        next_first = first.next
        next_slow = slow.next
        slow.next=next_first
        first.next=next_slow
        return head