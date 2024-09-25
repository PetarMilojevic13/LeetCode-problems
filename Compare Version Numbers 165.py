class Solution(object):

    def number_digits(self, number ):

        cnt = 1
        mask = 10

        while number//mask>0:
            cnt+=1
            mask*=10
        return cnt


    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        nums_1 = version1.split(".")
        print(nums_1)
        nums_2 = version2.split(".")
        print(nums_2)

        if len(nums_1)<len(nums_2):
            while len(nums_1)<len(nums_2):
                nums_1.append("0")
        if len(nums_2)<len(nums_1):
            while len(nums_2)<len(nums_1):
                nums_2.append("0")

        index = 0
        while index<len(nums_1):
            num1 = nums_1[index]
            num2 = nums_2[index]
            num1 = int(num1)
            num2 = int(num2)
            if num1<num2:
                return -1
            if num2<num1:
                return 1
            index+=1
        return 0

