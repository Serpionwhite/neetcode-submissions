# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        queue = deque()
        queue.append((root, root.val))
        total = 0

        while queue:
            current_element, max_value = queue.popleft()

            if current_element.val >= max_value:
                total += 1

            new_max = max(max_value, current_element.val)

            if current_element.left:
                queue.append((current_element.left, new_max))
            
            if current_element.right:
                queue.append((current_element.right, new_max))

        
        return total
        