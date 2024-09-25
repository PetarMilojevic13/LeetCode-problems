import heapq
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.priority_queue = []
        heapq.heapify(self.priority_queue)
        self.cnt_elements = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.cnt_elements+=1
        heapq.heappush(self.priority_queue,val)

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        self.cnt_elements-=1
        self.priority_queue.remove(element)
        heapq.heapify(self.priority_queue)
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
        print(self.priority_queue)
        element = self.priority_queue[0]
        return element

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()