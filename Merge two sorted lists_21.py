# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        first = list1
        second = list2
        head = None
        current = None

        while first!=None and second!=None:

            if first.val<=second.val:
                if head==None:
                    head=first
                    current=head
                else:
                    current.next=first
                    current=first
                first=first.next
            else:
                if head==None:
                    head=second
                    current=head
                else:
                    current.next=second
                    current=second
                second = second.next

        while first!=None:
            if head==None:
                head=first
                current=head
                first = first.next
            else:
                current.next=first
                current = first
                first=first.next

        while second!=None:
            if head==None:
                head=second
                current=head
                second = second.next
            else:
                current.next=second
                current=second
                second=second.next
        return head