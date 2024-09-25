# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        #Level order

        if root==None:
            return None

        count = len(to_delete)

        queue = [(root,None)]
        nodes = []


        while len(queue)>0:
            node,parent = queue.pop(0)
            if node.val not in to_delete:
                nodes.append(node)
            else:
                if parent != None and parent.left == node:
                    parent.left = None
                elif parent!=None and parent.right==node:
                    parent.right=None


            if node.left != None:
                queue.append((node.left, node))
            if node.right != None:
                queue.append((node.right, node))
        res = []
        while len(nodes)>0:


            first = True
            queue_tree = [nodes[0]]
            while len(queue_tree)>0:
                node = queue_tree.pop(0)
                for index in range(len(nodes)):
                    if node==nodes[index]:
                        nodes.pop(index)
                        break
                if first:
                    res.append(node)
                    first=False
                if node.left!=None:
                    queue_tree.append(node.left)
                if node.right!=None:
                    queue_tree.append(node.right)

        return res




