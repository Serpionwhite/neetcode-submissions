# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False


        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True

            slow_pointer = slow_pointer.next

        
        return False
        