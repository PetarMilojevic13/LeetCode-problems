# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        counter = 0
        node = root
        stack = []
        while True:
            while node!=None:
                stack.append(node)
                node=node.left
            if len(stack)==0:
                break
            else:
                node = stack.pop()
                counter+=1
                if counter==k:
                    return node.val
                node=node.right
        return 0