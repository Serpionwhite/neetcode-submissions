class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_count = len(stones)
        if stone_count < 2:
            return stones[-1]

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)

            if first_stone != second_stone:
                heapq.heappush(max_heap, -(first_stone - second_stone))

        if not max_heap:
            return 0

        
        return -max_heap[0]

        

