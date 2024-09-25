from queue import PriorityQueue
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = set()
        array.add(1)
        for i in range(n-1):
            number = min(array)
            array.remove(number)
            for mul in (2, 3, 5):
                new_number = number*mul
                if new_number not in array:
                    array.add(new_number)
        return min(array)


# Press the green button in the gutter to run the script.
test = Solution()
print(test.nthUglyNumber(19))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
