# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr_head = head
        while curr_head is not None:
            next_node = curr_head.next
            curr_head.next = prev
            prev = curr_head
            curr_head = next_node

        return prev

        