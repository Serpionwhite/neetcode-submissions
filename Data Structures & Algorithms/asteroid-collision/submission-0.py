class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        total_asteroids = len(asteroids)
        stack = []

        for index in range(total_asteroids):

            while stack and (stack[-1] > 0 and asteroids[index] < 0):
                
                if abs(stack[-1]) < abs(asteroids[index]):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroids[index]):
                    stack.pop()
                
                break

            else:
                stack.append(asteroids[index])


        return stack

        