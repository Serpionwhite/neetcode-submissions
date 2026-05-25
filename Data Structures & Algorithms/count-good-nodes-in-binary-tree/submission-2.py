# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traversal(self, root, max_value):
        if root is None:
            return 0

        if root.val >= max_value:
            good = 1
        else:
            good = 0
        new_max = max(max_value, root.val)

        return good + self.traversal(root.left, new_max) + self.traversal(root.right, new_max)

        
        self.traversal(root)

    def goodNodes(self, root: TreeNode) -> int:

        return self.traversal(root, root.val)
        