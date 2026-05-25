class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        total_points = len(points)

        if total_points < 1:
            return []

        if total_points < 2:
            return [points]
        
        min_heap = []

        for coordinates in points:
            distance = math.sqrt((coordinates[0]**2) + (coordinates[1]**2))
            heapq.heappush(min_heap, (distance, coordinates))

        smallest_distance = heapq.nsmallest(k,min_heap)

        res = []

        for value in smallest_distance:
            res.append(value[-1])

        return res






        