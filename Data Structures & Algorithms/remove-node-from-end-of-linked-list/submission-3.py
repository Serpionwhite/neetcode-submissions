# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Step 1: Move fast n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Step 2: Move both together
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Remove node
        slow.next = slow.next.next

        return dummy.next
