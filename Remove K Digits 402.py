class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        current_num = num
        remaining_to_cut = k
        res = ""
        if num=="0":
            return "0"
        if len(num)==k:
            return "0"
        if len(num)-k==1:
            minimum = None
            for n in num:
                if minimum==None:
                    minimum=n
                else:
                    if int(minimum)>int(n):
                        minimum=n
            return minimum



        while remaining_to_cut>0 and len(res)<len(num)-k:
            current_zeros = 0
            if len(res)>0:
                minimum = int(current_num[0])
                i = 0
            else:
                minimum = int(current_num[0])
                i = 0

            if len(res)>0:
                for index in range(i + 1, 1 + remaining_to_cut):
                    if int(current_num[index])<minimum:
                        i=index
                        minimum = int(current_num[index])
            else:

                start = 1
                zero_counter=0
                while start >= 0:
                    if current_num[start] != "0":
                        break
                    zero_counter += 1
                    start -= 1
                if zero_counter > 0 and start + 1  + zero_counter > remaining_to_cut:
                    i = index
                    minimum = int(current_num[index])
                    current_zeros = start + 1 + zero_counter + zero_counter

                for index in range(i + 1, len(current_num)):
                        if int(current_num[index])<minimum and index<1 + remaining_to_cut and current_zeros==0 and current_num[index]!="0":
                            i=index
                            minimum = int(current_num[index])

            print(i)
            print(minimum)
            remaining_to_cut-=i
            res+=current_num[i]
            current_num=current_num[i+1:]
        if len(res)<len(num)-k:
            res+=current_num
        return res

test = Solution()
print(test.removeKdigits("112",1))




