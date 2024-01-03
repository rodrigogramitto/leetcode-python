class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        values = list()

        def dfs_preorder(node):
            values.append(node.val)
            if node.left:
                dfs_preorder(node.left)
            if node.right:
                dfs_preorder(node.right)
            return node
        dfs_preorder(root)
        return values