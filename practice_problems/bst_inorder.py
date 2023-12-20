class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = list()
        if root is None:
            return values

        def dfs(node):
            if node.left:
                dfs(node.left)
            values.append(node.val)
            if node.right:
                dfs(node.right)
            return node
        dfs(root)
        return values