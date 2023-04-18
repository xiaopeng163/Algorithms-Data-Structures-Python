# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        # in order DFS
        self.flag = 1
        self.pre_node = None

        def traversal(current_node):
            if self.flag != 1:
                return
            if current_node.left is not None:
                traversal(current_node.left)
            # results.append(current_node.val)
            if self.pre_node:
                if self.pre_node.val >= current_node.val:
                    self.flag = 0
            self.pre_node = current_node

            if current_node.right is not None:
                traversal(current_node.right)

        traversal(root)
        return True if self.flag == 1 else False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root)
