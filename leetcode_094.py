# Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        l = [] # as a stack
        res = []
        while node != None or len(l) > 0:
            while node != None:
                l.append(node)
                node = node.left
            node = l.pop()
            res.append(node.val)
            node = node.right
        return res