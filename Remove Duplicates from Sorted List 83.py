# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        while slow!=None:

            fast = slow.next
            while fast!=None and fast.val==slow.val:
                fast=fast.next
            slow.next=fast
            slow=slow.next
        return head