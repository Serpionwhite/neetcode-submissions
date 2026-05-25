class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-value for value in nums]

        heapq.heapify(max_heap)

        res = heapq.nsmallest(k, max_heap)

        return -res[-1]
        