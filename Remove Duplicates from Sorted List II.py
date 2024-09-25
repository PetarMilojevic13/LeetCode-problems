# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head
        prev = None
        while node!=None:
            if node.next!=None and node.next.val==node.val:
                next_one = node
                while next_one!=None and next_one.val==node.val:
                    next_one=next_one.next
                if prev!=None:
                    prev.next=next_one
                else:
                    head=next_one
                node=next_one
            else:
                prev = node
                node=node.next
        return head

test = Solution()

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(3)
L5 = ListNode(4)
L6 = ListNode(4)
L7 = ListNode(5)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=L6
L6.next=L7
test.deleteDuplicates(L1)