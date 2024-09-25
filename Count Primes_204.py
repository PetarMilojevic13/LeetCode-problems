class Solution(object):

    def isPrime(self,number):
        start = number//2
        end = 2

        while start>end:
            if number%start==0:
                return False
            start-=1
        return True


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<2:
            return 0
        if n==2:
            return 0
        counter = 1

        number = 3

        while number<n:
            if number%2==0:
                number+=1
            else:
                if(self.isPrime(number)):
                    counter+=1
                number+=1
        return counter
