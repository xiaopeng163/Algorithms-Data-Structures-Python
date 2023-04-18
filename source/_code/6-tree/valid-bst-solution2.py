# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return (
            low < root.val
            and root.val < high
            and self.isValidBSTRecu(root.left, low, root.val)
            and self.isValidBSTRecu(root.right, root.val, high)
        )
