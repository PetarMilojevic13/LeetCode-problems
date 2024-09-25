class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return []

        sum_rolls = 0
        for rol in rolls:
            sum_rolls+=rol

        total_sum = mean*(n+len(rolls))

        if total_sum-sum_rolls> n*6:
            return []
        elif total_sum-sum_rolls<n:
            return []
        else:
            res = []
            remaining_sum = total_sum-sum_rolls
            remaining_count = n
            for index in range(n):
                for num in range(6,0,-1):
                    if remaining_count>0 and remaining_sum-num>=remaining_count-1:
                        res.append(num)
                        remaining_sum-=num
                        remaining_count-=1
                        break
                    elif remaining_count==1:
                        res.append(remaining_sum)
                        break
                    else:
                        continue
            return res

test = Solution()
print(test.missingRolls([1,5,6],3,4))
