class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        first_sign_pos = True

        minimum = 2**30
        minimum = minimum*(-2)

        if dividend==minimum and divisor==-1:
            return 0-(minimum+1)

        if divisor==-1:
            return 0-dividend
        if divisor==1:
            return dividend




        if dividend<0:
            dividend = 0-dividend
            first_sign_pos = False
        second_sign_pos = True


        if divisor<0:
            divisor = 0-divisor
            second_sign_pos = False

        count = 0

        while dividend >= divisor:
            x = 1
            base = divisor
            while (base<<1) <= (dividend):
                base <<= 1
                x <<= 1
            count += x
            dividend -= base


        if first_sign_pos!=second_sign_pos:
            count = 0 - count
        return count
