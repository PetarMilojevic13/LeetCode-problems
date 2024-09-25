# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print(lists)
        for n in lists:
            try:
                lists.index(None)
                lists.remove(None)
            except:
                break


        head = None
        previous = None
        while len(lists)>0:
            found = False
            minimum = None
            node_min = None
            minimum_index = -1
            for node in lists:
                if node!=None:
                    if found==False:
                        found=True
                        minimum=node.val

                        node_min=node
                        minimum_index = lists.index(node)
                    else:
                        if node.val<minimum:

                            node_min=node
                            minimum=node.val

                            minimum_index = lists.index(node)
            if found==False:
                break
            if head==None:
                head=node_min
                previous=head
                lists[minimum_index] = node_min.next
            else:
                previous.next=node_min
                previous=node_min
                lists[minimum_index]=node_min.next
                if lists[minimum_index]==None:
                    lists.pop(minimum_index)
        return head

test = Solution()

arr = []

L = ListNode(5)
L2 = ListNode(4,L)
L3 = ListNode(1,L2)
arr.append(L3)

L = ListNode(4)
L2 = ListNode(3,L)
L3 = ListNode(1,L2)
arr.append(L3)

L = ListNode(5)
L2 = ListNode(6)
L3 = ListNode(2,L2)
arr.append(L3)


a = test.mergeKLists(arr)

while a!=None:
    print(a.val)
    a=a.next
