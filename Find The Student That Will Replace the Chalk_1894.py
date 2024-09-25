class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        index = 0
        last = 0

        sum = 0
        for i in range(len(chalk)):
            sum+=chalk[i]
        k = k%sum



        while k>=0:
            k-=chalk[index]
            last = index
            index+=1
            index = index%len(chalk)
        return last