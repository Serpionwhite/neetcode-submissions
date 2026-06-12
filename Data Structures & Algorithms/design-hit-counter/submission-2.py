class HitCounter:

    def __init__(self):
        self.hit_queue = deque()
        self.hit_counter = {}
        

    def hit(self, timestamp: int) -> None:
        if timestamp in self.hit_counter:
            self.hit_counter[timestamp] += 1

        else:
            self.hit_queue.append(timestamp)
            self.hit_counter[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        start_timer = timestamp - 300 if timestamp > 300 else 0
        while self.hit_queue and self.hit_queue[0] <= start_timer:
            remove_stamp = self.hit_queue.popleft()
            del self.hit_counter[remove_stamp]

        return sum(self.hit_counter.values())
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
