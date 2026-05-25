# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.left_height = 0
        self.right_height = 0
        self.flag = True
        
        def traversal(root):
            if root is None:
                return 0

            left = traversal(root.left)
            right = traversal(root.right)


            if abs(left-right) > 1:
                self.flag = False

            return 1 + max(left, right)
        traversal(root)
        return self.flag

            

        
        