class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maximum = 0
        index = 0
        counter = 0
        fruits_set = []
        while True:
            if index==len(fruits):
                if counter > maximum:
                    maximum = counter
                return maximum
            else:
                if (fruits[index] in fruits_set):
                    counter+=1
                    index+=1
                elif len(fruits_set)<2:
                    fruits_set.append(fruits[index])
                    counter+=1
                    index += 1
                else:
                    if counter>maximum:
                        maximum=counter

                    if fruits[index-1]==fruits_set[0]:
                        fruits_set.pop(1)
                    else:
                        fruits_set.pop(0)
                    auxiliary_index = index - 1
                    cnt = 0
                    while auxiliary_index >= 0 and fruits[auxiliary_index] == fruits[index - 1]:
                        cnt += 1
                        auxiliary_index -= 1
                    counter = cnt


        return maximum
test = Solution()
print(test.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))