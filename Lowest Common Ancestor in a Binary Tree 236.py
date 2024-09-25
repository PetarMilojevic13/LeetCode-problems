# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # tuple - height,node,father
        queue = [(0, root, None)]
        all_nodes = []
        node_p = None
        node_q = None
        height_p = -1
        height_q = -1

        while len(queue) > 0 and (node_p == None or node_q == None):
            height, node, father = queue.pop(0)
            all_nodes.append((height, node, father))
            if node == p:
                node_p = node
                height_p = height
            if node == q:
                node_q = node
                height_q = height
            if node.left != None:
                queue.append((height + 1, node.left, node))
            if node.right != None:
                queue.append((height + 1, node.right, node))

        current_height_p = height_p
        current_height_q = height_q


        while current_height_p != current_height_q:
            if current_height_q > current_height_p:
                for tup in all_nodes:
                    if tup[1] == node_q:
                        node_q = tup[2]
                        current_height_q -= 1
                        break
            elif current_height_p > current_height_q:
                for tup in all_nodes:
                    if tup[1] == node_p:
                        node_p = tup[2]
                        current_height_p -= 1
                        break

        while node_p != node_q:

            for tup in all_nodes:
                if tup[1] == node_p:
                    node_p = tup[2]
                    break

            for tup in all_nodes:
                if tup[1] == node_q:
                    node_q = tup[2]
                    break

        return node_p


