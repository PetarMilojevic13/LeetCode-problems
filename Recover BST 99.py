# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        prev = None
        node = root
        stack = []
        found_error = False
        start_error = None
        end_error = None
        while True:
            while node != None:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                if prev != None:
                    if node.val<prev.val:
                        if found_error == False:
                            found_error = True
                            start_error = prev

                        end_error = node
                prev = node
                node = node.right
            else:
                break

        tmp = start_error.val
        start_error.val = end_error.val
        end_error.val = tmp
        return root