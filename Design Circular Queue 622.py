class Node(object):
    def __init__(self,val,node=None):
        self.val = val
        self.next = node

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.current_number_nodes = 0
        self.limit = k
        self.head = None
        self.tail = None


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.current_number_nodes == self.limit:
            return False
        node = Node(value)
        self.current_number_nodes += 1
        if self.tail==None:
            self.tail=node
            self.head=node
        else:
            self.tail.next = node
            self.tail=node

        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.current_number_nodes==0:
            return False

        self.current_number_nodes-=1
        self.head = self.head.next
        if self.current_number_nodes==0:
            self.tail=None
        return True
    def Front(self):
        """
        :rtype: int
        """
        if self.current_number_nodes==0:
            return -1

        return self.head.val
    def Rear(self):
        """
        :rtype: int
        """
        if self.current_number_nodes==0:
            return -1
        return self.tail.val
    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.current_number_nodes==0:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.current_number_nodes==self.limit:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()