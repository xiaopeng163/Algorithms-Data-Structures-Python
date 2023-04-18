# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        if root.left:
            if root.val <= self.find_max(root.left):
                return False
        if root.right:
            if root.val >= self.find_min(root.right):
                return False

        if self.isValidBST(root.left) and self.isValidBST(root.right):
            return True
        return False

    def find_max(self, root):

        # 最大值在右子树的最右一个节点
        while root.right:
            root = root.right
        return root.val

    def find_min(self, root):
        while root.left:
            root = root.left

        return root.val
