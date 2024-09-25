class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        mapping = dict()

        mapping = {1000:"M", 500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

        max_divider = 1
        while num//max_divider>0:
            max_divider*=10
        max_divider//=10
        current_num = num
        roman_num = ""
        while current_num>0:
            biggest_digit = current_num//max_divider
            if biggest_digit==4:
                roman_num+=mapping[max_divider]
                biggest_digit=5
            elif biggest_digit==9:
                roman_num+=mapping[max_divider]
                biggest_digit=10



            current_roman = biggest_digit*max_divider

            while current_roman>0:
                current_max=0
                for key in mapping.keys():
                    if(current_roman//key>0) and (key>current_max):
                        current_max=key
                roman_num+=mapping[current_max]
                current_roman-=current_max



            current_num = current_num%max_divider
            max_divider = max_divider//10

        return roman_num


test = Solution()
print(test.intToRoman(3749))