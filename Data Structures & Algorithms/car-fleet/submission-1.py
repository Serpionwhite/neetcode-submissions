class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total_cars = len(position)

        if target == 0:
            return total_cars

        if total_cars < 2:
            return 1

        pairs = sorted(zip(position, speed), reverse = True)
        stack = []

        for position, speed in pairs:
            time = (target-position) / speed
            if stack and time <= stack[-1]:
                continue

            stack.append(time)



        return len(stack)
