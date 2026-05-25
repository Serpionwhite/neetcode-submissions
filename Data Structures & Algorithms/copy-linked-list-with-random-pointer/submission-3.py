"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        
        temp = head
        hash_map = {}

        while temp:
            hash_map[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            copy = hash_map[temp]
            copy.next = hash_map.get(temp.next)
            copy.random = hash_map.get(temp.random)
            temp = temp.next

        return hash_map[head]

        

        