# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        prev = None
        while fast!=None and fast.next!=None:
            prev = slow
            slow=slow.next
            fast=fast.next
            fast=fast.next

        if slow==head:
            head = head.next
        else:
            prev.next=slow.next
        return head