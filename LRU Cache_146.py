from collections import deque
class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = capacity
        self.current_capacity = 0
        self.cache = dict()
        self.LRU = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.current_capacity < self.capacity:
            if key not in self.cache.keys():
                self.current_capacity+=1
                self.LRU.append(key)
            else:
                self.LRU.remove(key)
                self.LRU.append(key)

            self.cache[key] = value
        else:
            if key not in self.cache.keys():
                deleting = self.LRU.popleft()
                del self.cache[deleting]
                self.cache[key] = value
                self.LRU.append(key)
            else:
                self.cache[key] = value
                self.LRU.remove(key)
                self.LRU.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)