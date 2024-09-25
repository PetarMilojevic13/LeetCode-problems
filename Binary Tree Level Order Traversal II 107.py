# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        queue = [[root]]
        res = [[root]]
        while len(queue) > 0:
            level = queue.pop(0)

            r = []
            for g in level:
                r.append(g.val)
            res.insert(0, r)

            next_level = []
            for node in level:
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)

            if len(next_level) > 0:
                queue.append(next_level)

        return res