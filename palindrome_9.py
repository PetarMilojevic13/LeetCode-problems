class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True

        number_down = x
        number_up = x

        mask = 10

        while x>=mask:
            mask = mask*10

        mask = mask / 10
        mask = int(mask)

        while number_down>0:
            digit_up = (number_up//mask)%10
            digit_down = number_down % 10
            number_down = number_down//10
            mask = mask//10
            if(digit_up!=digit_down):
                return False
        return True

test = Solution()
print(test.isPalindrome(123))