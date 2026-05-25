# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        count = 0

        while queue:
            for index in range(len(queue)):
                current_element = queue.popleft()
                if current_element.left:
                    queue.append(current_element.left)
                if current_element.right:
                    queue.append(current_element.right)
            count += 1

        return count