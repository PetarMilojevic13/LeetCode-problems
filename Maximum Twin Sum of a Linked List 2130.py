# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = head
        slow = head
        prev = None
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            prev=slow
            slow=slow.next

        next_node = slow
        mid = prev

        reversal = head
        prev = None
        while reversal!=next_node:
            next_one = reversal.next
            reversal.next=prev
            prev=reversal
            reversal=next_one
        maximum = -1
        while mid!=None:
            sum_tot =  mid.val+next_node.val
            maximum=max(maximum,sum_tot)
            mid=mid.next
            next_node=next_node.next
        return maximum



