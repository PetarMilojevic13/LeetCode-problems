class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        index = len(nums)-1
        found = None
        while index>=0:
            j = index+1
            num = nums[index]
            min = None
            index_found = None
            while j<len(nums):
                if nums[j]>num and (min==None or nums[j]<min):
                    min = nums[j]
                    index_found=j
                j+=1
            if min!=None:
                min = nums.pop(index_found)
                nums.insert(index,min)
                found=index
                break
            index-=1


        if found==None:
            end = len(nums)//2
            index = 0
            while index<end:
                tmp = nums[len(nums)-1-index]
                nums[len(nums)-1-index]=nums[index]
                nums[index]=tmp
                index+=1
            return
        else:
            start = found+1
            while start<len(nums):
                index = start+1
                min = nums[start]
                index_min = start
                while index<len(nums):
                    if nums[index]<min:
                        min = nums[index]
                        index_min=index
                    index+=1
                nums[index_min]=nums[start]
                nums[start]=min
                start+=1
            return

test = Solution()
nums = [5,4,7,5,3,2]
test.nextPermutation(nums)
print(nums)