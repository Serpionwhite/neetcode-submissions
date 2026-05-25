# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res

        queue = deque()
        queue.append(root)
        res.append([root.val])
        level = 0

        while len(queue) > 0:
            temp_res = []
            for index in range(len(queue)):
                current_element = queue.popleft()
                
                if current_element.left:
                    queue.append(current_element.left)
                    temp_res.append(current_element.left.val)

                if current_element.right:
                    queue.append(current_element.right)
                    temp_res.append(current_element.right.val)

                
            if temp_res:
                res.append(temp_res)
            level += 1

        return res