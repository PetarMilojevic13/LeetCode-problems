# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root==None:
            return []
        queue = [[root]]
        res = []

        while len(queue)>0:
            level = queue.pop(0)
            r= []
            for l in level:
                r.append(l.val)

            res.append(r)
            next_lev = []
            for node in level:
                if node.left!=None:
                    next_lev.append(node.left)
                if node.right!=None:
                    next_lev.append(node.right)
            if len(next_lev)>0:
                queue.append(next_lev)

        return res