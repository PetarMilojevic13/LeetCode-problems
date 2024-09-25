# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        queue = []
        queue.append(root)
        tree_current = None
        possible_roots = []
        while len(queue)>0:
            tree_current = queue.pop(0)
            if tree_current.val==head.val:
                possible_roots.append(tree_current)
            if tree_current.left!=None:
                queue.append(tree_current.left)
            if tree_current.right!=None:
                queue.append(tree_current.right)

        if len(queue)==0:
            return False

        while len(possible_roots)>0:
            list_current = head
            tree_current = possible_roots.pop(0)

            current_pairs = [(tree_current,list_current)]
            while len(current_pairs)>0:
                print(current_pairs)
                tree_current, list_current = current_pairs.pop(0)
                if list_current.next==None:
                    return True
                if tree_current.left!=None and tree_current.left.val == list_current.next.val:
                    current_pairs.append((tree_current.left,list_current.next))
                if tree_current.right!=None and tree_current.right.val == list_current.next.val:
                    current_pairs.append((tree_current.right, list_current.next))


        return False

test = Solution()