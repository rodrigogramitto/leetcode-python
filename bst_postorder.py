class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        values = list()

        def dfs_postorder(node):
            if node.left:
                dfs_postorder(node.left)
            if node.right:
                dfs_postorder(node.right)
            return values.append(node.val)

        dfs_postorder(root)
        return values