# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Level - Order
        if root==None:
            return []
        queue = [[root]]
        res = []

        while len(queue)>0:
            level = queue.pop(0)
            maximum = level[0].val
            next_level = []
            for num in level:
                if num.val>maximum:
                    maximum=num.val
                if num.left!=None:
                    next_level.append(num.left)
                if num.right!=None:
                    next_level.append(num.right)

            res.append(maximum)
            if len(next_level)>0:
                queue.append(next_level)
        return res
