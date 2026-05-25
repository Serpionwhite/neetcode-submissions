# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def traversal(node):
            if not node:
                return 0

            left = traversal(node.left)
            right = traversal(node.right)

            if node:
                self.length = max(self.length, 1 + left + right)
                return 1 + max(left,right)
            
            return 

        traversal(root)

        return self.length-1
        