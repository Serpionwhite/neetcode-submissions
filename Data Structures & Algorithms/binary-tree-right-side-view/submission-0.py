# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if root is None:
            return res

        res.append(root.val)
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for index in range(len(queue)):
                current_element = queue.popleft()

                if current_element.left:
                    queue.append(current_element.left)
                
                if current_element.right:
                    queue.append(current_element.right)

            
            if queue:
                res.append(queue[-1].val)

        return res
        