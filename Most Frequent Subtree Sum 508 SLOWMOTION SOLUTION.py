# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def TreeSum(self, root):
        left_sum = 0
        if root.left != None:
            left_sum = self.TreeSum(root.left)
        right_sum = 0
        if root.right != None:
            right_sum = self.TreeSum(root.right)
        return root.val + left_sum + right_sum

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hashmap = dict()
        stack = []
        current = root
        maximum = 0
        while True:
            while current != None:
                stack.append(current)
                current = current.left
            if len(stack) > 0:
                current = stack.pop()

                sum = self.TreeSum(current)
                if sum not in hashmap.keys():
                    hashmap[sum] = 1
                    if maximum<1:
                        maximum=1
                else:
                    hashmap[sum] += 1
                    if maximum<hashmap[sum]:
                        maximum=hashmap[sum]
                current = current.right
            else:
                break
        res = []
        for k in hashmap.keys():
            if hashmap[k]==maximum:
                res.append(k)
        return res
