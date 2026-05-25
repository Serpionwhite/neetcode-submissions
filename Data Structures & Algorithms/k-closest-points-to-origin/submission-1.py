class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        total_points = len(points)

        if total_points < 1:
            return []

        if total_points < 2:
            return points
        
        min_heap = [(x**2 + y**2, [x,y]) for x,y in points]
        heapq.heapify(min_heap)

        res = []

        for index in range(k):
            _, point = heapq.heappop(min_heap)
            res.append(point)
        return res






        