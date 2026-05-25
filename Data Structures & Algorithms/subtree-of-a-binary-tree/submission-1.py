# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if (root1 and not root2) or (not root1 and root2):
            return False

        if root1.val != root2.val:
            return False

        left = self.isSameTree(root1.left, root2.left)
        right = self.isSameTree(root1.right, root2.right)

        return left and right


    def dfs(self,root):
        queue = deque()
        queue.append(root)
        res_queue = deque()

        while queue:
            current_element = queue.popleft()
            res_queue.append(current_element)
            
            if current_element.left:
                queue.append(current_element.left)

            if current_element.right:
                queue.append(current_element.right)

        return res_queue



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        if (root and not subRoot) or (not root and subRoot):
            return False

        
        queue = deque()
        queue.append(root)
        start_point = None

        while queue:
            current_element = queue.popleft()
            if current_element.val == subRoot.val:
                start_point = current_element
                break
            
            if current_element.left:
                queue.append(current_element.left)

            if current_element.right:
                queue.append(current_element.right)

        if start_point is None:
            return False

        tree1 = self.dfs(start_point)
        tree2 = self.dfs(subRoot)
        flag = False

        while tree1:
            tree1_element = tree1.popleft()
            if tree1_element.val == subRoot.val:
                check = self.isSameTree(tree1_element, subRoot)
                if check:
                    flag = True
                    break



        return flag


        
        