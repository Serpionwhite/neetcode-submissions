# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root, root1, res):
        if root is None:
            return False

        res.append(root)

        if root == root1:
            return True

        left = self.traversal(root.left, root1, res)
        right = self.traversal(root.right, root1, res)

        if left or right:
            return True

        res.pop()

        return False

        

        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left

            elif p.val > root.val and q.val > root.val:
                root = root.right

            else:
                return root

        