# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        set_nums = set()
        for num in nums:
            set_nums.add(num)


        current = head
        prev = None
        if head==None:
            return head

        while current!=None:
            if current.val in set_nums:
                if prev == None:
                    head = head.next
                    old = current
                    current = head
                    old.next = None
                else:
                    prev.next = current.next
                    old = current
                    current = current.next
                    old.next = None
            else:
                prev = current
                current=current.next
        return head

