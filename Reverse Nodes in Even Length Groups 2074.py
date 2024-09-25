# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        full_total = 0
        while current!=None:
            full_total+=1
            current=current.next

        last_group_cnt = full_total
        group_cnt = 0
        for i in range(full_total):
            if last_group_cnt-i<=0:
                break
            else:
                last_group_cnt-=i
                group_cnt+=1



        current = head
        counter = 1
        current_group = 1
        prev_group = None
        first_group = None
        prev = None

        while current!=None:

            if (current_group%2==0 and current_group<group_cnt) or (current_group==group_cnt and last_group_cnt%2==0):
                next_one = current.next
                current.next=prev
                prev=current

                if counter==1:
                    first_group=current



                if counter==current_group or next_one==None:
                    prev_group.next=current
                    first_group.next=next_one
                    prev_group=first_group
                    current_group += 1
                    counter = 1

                else:
                    counter += 1
                current=next_one

            else:
                prev_group=current
                prev = current

                if counter==current_group:
                    current = current.next
                    current_group+=1
                    counter=1
                else:
                    current = current.next
                    counter+=1
        return head

test = Solution()
prev = None
head = None
array = [4,3,0,5,1,2,7,8,6]
for num in array:
    current = ListNode(num)
    if prev!=None:
        prev.next=current
    else:
        head=current
    prev = current
node = test.reverseEvenLengthGroups(head)
while node!=None:
    print(node.val)
    node=node.next


