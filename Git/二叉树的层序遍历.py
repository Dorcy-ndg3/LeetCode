# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        #递归
        def add_to_result(level, node):
            if level > len(result) - 1:
                result.append([]) 
            result[level].append(node.val)
            if node.left:
                add_to_result(level+1, node.left)
            if node.right:
                add_to_result(level+1, node.right)
        add_to_result(0, root)
        return result