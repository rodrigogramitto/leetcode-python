# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
#         curr = root

#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             k -= 1
#             if k == 0:
#                 return curr.val
#             curr = curr.right


# non optimal but my idea

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        if root is None:
            return None

        def dfs_inorder(node):
            if node is not None:
                dfs_inorder(node.left)
                values.append(node.val)
                dfs_inorder(node.right)

        dfs_inorder(root)
        return values[k - 1]