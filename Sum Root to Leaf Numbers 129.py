# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Preorder
        if root == None:
            return 0
        stack = [(root,"")]
        string_current = ""
        node = root
        sumarum = 0
        while len(stack)>0:
            node,string_current = stack.pop()
            prev = None
            while node!=None:
                prev = node
                string_current += str(node.val)
                if node.right!=None:
                    stack.append((node.right,string_current))
                node=node.left
            if prev.right==None:
                sumarum+=int(string_current)
        return sumarum

