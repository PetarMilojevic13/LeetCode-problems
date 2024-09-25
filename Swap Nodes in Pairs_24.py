# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        final_count = 0
        node = head
        while node != None:
            final_count += 1
            node = node.next
        final_count = final_count // 2
        final_count = final_count * 2

        first = True
        current = head
        previous = None
        start = head
        counter = 1
        prev_start = None
        index = 0

        while index < final_count:
            if counter == 2:
                next_one = current.next
                start.next = next_one
                if previous != None:
                    current.next = previous

                if first:
                    first = False
                    head = current
                    prev_start = start
                else:
                    prev_start.next = current
                    prev_start = start

                counter = 1
                previous = None
                current = next_one
                start = current
                index += 1
            else:
                counter += 1
                next_one = current.next
                if previous != None:
                    current.next = previous

                previous = current
                current = next_one
                index += 1
        return head