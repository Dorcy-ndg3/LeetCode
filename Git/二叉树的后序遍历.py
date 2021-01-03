class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 后序递归
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
