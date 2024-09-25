# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        if head==None or head.next==None:
            return True


        fast = head
        slow = head
        prev = None
        while fast!=None and fast.next!=None:

            #Reverse
            next_one = slow.next
            slow.next=prev

            #Continuation
            prev=slow
            print(fast)
            print(slow)
            if slow==head:
                fast=next_one.next
            else:
                fast=fast.next.next
            slow=next_one


        if fast==None:
            fast=slow
        else:
            fast=slow.next
        slow=prev

        while slow!=None:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True