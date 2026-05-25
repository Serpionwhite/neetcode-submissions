# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root, min_value, max_value):
        if root is None:
            return True

        if not (min_value < root.val < max_value):
            return False

            
        return self.traversal(root.left, min_value, root.val) and self.traversal(root.right, root.val, max_value)


            

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.traversal(root, float("-inf"), float("inf"))
        