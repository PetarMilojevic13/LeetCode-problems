class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        index1 = 0
        index2 = 0
        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1]==nums2[index2]:
                return nums1[index1]
            if nums1[index1]<nums2[index2]:
                index1+=1
            else:
                index2+=1
        return -1
