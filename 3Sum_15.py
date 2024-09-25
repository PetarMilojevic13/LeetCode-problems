class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_set=[]
        hash_map = dict()
        set_nums=[]
        for i in range(len(nums)):
            if nums[i] in hash_map.keys():
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        for i in range(len(hash_map.keys())):
            list_key = list(hash_map.keys())

            num = list_key[i]
            hash_map[num]-=1
            two_sum = 0-num

            #Different_numbers
            for j in range(i,len(list_key)):
                if (hash_map[list_key[j]]>0):
                    hash_map[list_key[j]] -= 1
                    current_num = two_sum-list_key[j]
                    try:
                        if hash_map[current_num]>0:
                            array_res = [list_key[i],list_key[j],current_num]
                            array_res.sort()
                            if array_res not in res_set:
                                res_set.append(array_res)
                        hash_map[list_key[j]]+=1
                    except:
                        hash_map[list_key[j]] += 1
                        continue
            hash_map[list_key[i]]+=1
        return res_set

test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4]))

