class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left<right:
            if left_max<right_max:
                left+=1
                left_max = max(left_max,height[left])
                water += height[left]-left_max
            else:
                right-=1
                right_max = max(right_max,height[right])
                water += height[right]-right_max
        return water


test = Solution()
print(test.trap([0,1,0,2,1,0,1,3,2,1,2,1]))