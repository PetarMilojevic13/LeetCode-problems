# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #POST-ORDER
        value = -2000
        node = root
        stack = []

        while node!=None:
            stack.append((node,False))
            node = node.left


        while len(stack)>0:




            node,flag = stack.pop()
            if flag==False:
                stack.append((node,True))
                node = node.right

                while node != None:
                    stack.append((node, False))
                    node = node.left

            else:
                set_sum = []
                left_sum = -2000
                if node.left!=None:
                    left_sum = node.left.val

                    set_sum.append(left_sum+node.val)
                right_sum = -2000
                if node.right!=None:
                    right_sum = node.right.val

                    set_sum.append(right_sum + node.val)
                set_sum.append(node.val)
                maximum = node.val
                for m in set_sum:
                    if m>maximum:
                        maximum=m
                old  = node.val
                node.val=maximum

                if maximum>value:
                    value = maximum
                if left_sum != -2000 and right_sum != -2000:
                    sum_all_3 = left_sum + right_sum + old
                    if sum_all_3>value:
                        value=sum_all_3





        return value

L1 = TreeNode(1)
L2 = TreeNode(2)
L3 = TreeNode(3)
L1.left=L2
L1.right=L3
test= Solution()
print(test.maxPathSum(L1))




