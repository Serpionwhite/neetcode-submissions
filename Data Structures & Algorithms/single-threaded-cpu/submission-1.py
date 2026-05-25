class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_length = len(tasks)
        processing_heap = []
        enque_heap = []


        for index in range(task_length):
            heapq.heappush(enque_heap, (tasks[index][0], tasks[index][1], index))

        current_time = 0
        res = []

        while enque_heap or processing_heap:
            if not processing_heap and enque_heap[0][0] > current_time:
                current_time = enque_heap[0][0]

            while enque_heap and enque_heap[0][0] <= current_time:
                eq, ep, ei = heapq.heappop(enque_heap) 
                heapq.heappush(processing_heap,(ep, ei))

            if processing_heap:
                task = heapq.heappop(processing_heap)
                current_time += task[0]
                res.append(task[1])
        

        return res
