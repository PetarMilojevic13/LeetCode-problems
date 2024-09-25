class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        descending_height = height.copy()
        descending_height.sort(reverse=True)
        if height.copy()==descending_height:
            return 0

        index = 0
        while True:
            if index>=len(height) or height[index]!=0:
                break
            else:
                height.pop(0)
        index = 0
        surface = 0
        while index<len(height):
            value_left = height[index]
            next = index+1
            current_max = 0
            current_max_index = -1
            while next<len(height) and height[next]<value_left:
                if height[next]>current_max:
                    current_max=height[next]
                    current_max_index=next
                next+=1
            if next==len(height):
                if current_max_index == -1:
                    break
                sum_surface = 0
                current = index+1
                while current<current_max_index:
                    sum_surface+=current_max-height[current]
                    current+=1
                surface+=sum_surface

                index = current_max_index
            else:
                sum_surface = 0
                current = index+1
                while current<next:
                    sum_surface+=value_left-height[current]
                    current+=1
                surface+=sum_surface
                index = next
        return surface

test = Solution()
print(test.trap([0,1,0,2,1,0,1,3,2,1,2,1]))