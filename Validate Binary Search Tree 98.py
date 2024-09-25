# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = []
        node = root
        current_value = None
        prev_value = None

        while True:
            while node!=None:
                stack.append(node)
                node = node.left
            if len(stack)>0:
                node = stack.pop()
                print(node.val)
                current_value = node.val
                if prev_value == None:
                    prev_value=current_value
                else:
                    if current_value<=prev_value:
                        return False
                    prev_value = current_value
                node = node.right
            else:
                break
        return True