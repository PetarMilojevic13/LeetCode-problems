class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = []
        index1 = 0
        index2 = 0
        while index1<len(nums1) or index2<len(nums2):
            if(index1>=len(nums1)):
                array.append(nums2[index2])
                index2+=1
            elif index2>=len(nums2):
                array.append(nums1[index1])
                index1+=1
            else:
                if(nums1[index1]<nums2[index2]):
                    array.append(nums1[index1])
                    index1+=1
                else:
                    array.append(nums2[index2])
                    index2+=1

        if len(array)%2==1:
            return array[len(array)/2]
        else:
            sum = array[(len(array)/2)-1] + array[(len(array)/2)]
            return sum/2.0

