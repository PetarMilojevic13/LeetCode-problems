#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        counter = 0
        current = head
        while current!=None:
            counter+=1
            current=current.next
        result = []
        for i in range(k):
            result.append(None)

        if head==None:
            return result

        current = head
        total_counter = 0
        part_counter = 0
        counter_in_part=0
        first = head

        if k==0:
            return [None]

        if k==1:
            result[0]=head
            return result


        number_of_nodes = []

        for index in range(k):
            number_of_nodes.append(counter//k)
        for index in range(counter%k):
            number_of_nodes[index]+=1

        while total_counter<counter and current!=None:

            if number_of_nodes[part_counter]-1==counter_in_part :
                next_one = current.next
                result[part_counter]=first
                current.next=None
                first=next_one
                current=next_one
                counter_in_part=0
                part_counter += 1

            else:
                current=current.next
                counter_in_part+=1


            total_counter+=1
        return result

head = None
prev = None
for index in range(10):
    node = ListNode(index+1)
    if prev==None:
        head=node
        prev=node
    else:
        prev.next=node
        prev=node
test = Solution()
test.splitListToParts(head,3)
