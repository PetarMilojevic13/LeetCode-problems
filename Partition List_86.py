# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
     self.val = val
     self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        first_larger = None
        current = head
        prev_larger = None
        smaller = None
        while current!=None:
            if current.val>=x:
                first_larger=current
                break
            prev_larger = current
            current = current.next
        prev = first_larger
        if first_larger!=None:
            smaller = first_larger.next

        while smaller!=None:
            if smaller.val<x:
               if prev_larger==None:
                   head = smaller
                   next_one = smaller.next
                   prev.next=smaller.next
                   smaller.next=first_larger
                   prev_larger=smaller
                   smaller = next_one
               else:
                    next_one = smaller.next
                    prev_larger.next = smaller
                    prev_larger = smaller
                    prev.next = smaller.next
                    smaller.next = first_larger
                    smaller = next_one
            else:
                prev=smaller
                smaller=smaller.next


        return head

test = Solution()

# L1 = ListNode(1)
# L2 = ListNode(4)
# L3 = ListNode(3)
# L4 = ListNode(2)
# L5 = ListNode(5)
# L6 = ListNode(2)
#
# L1.next=L2
# L2.next=L3
# L3.next=L4
# L4.next=L5
# L5.next=L6

L1 = ListNode(2)
L2 = ListNode(1)
L1.next=L2

L = test.partition(L1,2)
while L!=None:
    print(L.val)
    L=L.next