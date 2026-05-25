# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None or (head.next is None and n== 1):
            return None

        curr_head = head
        count = 0

        while curr_head:
            count += 1
            curr_head = curr_head.next

        if count == n:
            return head.next

        temp = head
        for index in range(count-n-1):
            temp = temp.next

        if temp.next is None or temp.next.next is None:
            temp.next = None
        else:
            temp.next = temp.next.next

        return head

  