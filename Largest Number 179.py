class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        first_digit = []
        for index in range(len(nums)):
            number = str(nums[index])
            first_digit.append(number)

        for i in range(len(first_digit)):
            for j in range(i,len(first_digit)):
                if first_digit[j]+first_digit[i]>first_digit[i]+first_digit[j]:
                    tmp = first_digit[i]
                    first_digit[i]=first_digit[j]
                    first_digit[j]=tmp

        res = ""
        for dig in first_digit:
            res+=dig
        if res[0]=="0":
            res="0"
        return res

test = Solution()
print(test.largestNumber([3,30,34,5,9]))