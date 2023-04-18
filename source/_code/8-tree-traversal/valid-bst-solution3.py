# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        # in order DFS
        results = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            results.append(current_node.val)
            if current_node.right is not None:
                traversal(current_node.right)

        traversal(root)
        return results

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        results = self.dfs(root)

        i = 1
        flag = 1
        while i < len(results):
            if results[i] <= results[i - 1]:
                flag = 0
                break
            i += 1
        return True if flag == 1 else False
