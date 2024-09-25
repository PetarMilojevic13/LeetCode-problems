class Node(object):
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.cnt_elem = 0
        self.tail = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.cnt_elem:
            return -1
        node = self.head
        cnt = 0
        while node != None:
            if cnt == index:
                return node.val
            else:
                cnt += 1
                node = node.next
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.cnt_elem += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)

        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.cnt_elem += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        if index > self.cnt_elem:
            return None

        if index == self.cnt_elem:
            self.addAtTail(val)
            return None

        new_node = Node(val)
        node = self.head
        cnt = 0
        prev = None
        while node != None:
            if cnt == index:
                if prev == None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    prev.next = new_node
                    new_node.next = node
                self.cnt_elem += 1
                return
            else:
                cnt += 1
                prev = node
                node = node.next

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if index >= self.cnt_elem:
            return None
        node = self.head
        cnt = 0
        prev = None
        while node != None:
            if cnt == index:
                if prev == None:
                    self.head = node.next
                else:
                    prev.next = node.next
                if index == self.cnt_elem - 1:
                    self.tail = prev
                self.cnt_elem -= 1
                return
            else:
                cnt += 1
                prev = node
                node = node.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)