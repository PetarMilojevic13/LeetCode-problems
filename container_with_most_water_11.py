class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height)-1
        max_height = 0
        while(left<right):
            x = right-left
            y = min(height[left],height[right])
            surface = int(x*y)
            if surface>max_height:
                max_height=surface
            if y==height[left]:
                left+=1
            else:
                right-=1
        return max_height