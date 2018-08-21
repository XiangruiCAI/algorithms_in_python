# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTreeRecursive({}, 1, n)
    
    def genTreeRecursive(self, mem, start, end):
        if start > end:
            return [None]
        if (start, end) in mem:
            return mem[(start, end)]
        mem[(start, end)] = []
        for root_val in range(start, end + 1):
            for left in self.genTreeRecursive(mem, start, root_val - 1):
                for right in self.genTreeRecursive(mem, root_val + 1, end):
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    mem[(start, end)].append(root)
        return mem[(start, end)]
