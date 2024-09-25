import heapq
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.priority_queue = []
        self.cnt_elements = 0
        self.minimum = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.cnt_elements+=1

        if self.minimum==None:
            self.minimum=val
        else:
            if self.minimum>val:
                self.minimum=val

        self.priority_queue.append(self.minimum)

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        self.cnt_elements-=1
        self.priority_queue.pop()

        if self.cnt_elements==0:
            self.minimum=None
        else:
            self.minimum = self.priority_queue[self.cnt_elements-1]
        return element

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.cnt_elements-1]

    def getMin(self):
        """
        :rtype: int
        """
        element = self.priority_queue[self.cnt_elements-1]
        return element

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()