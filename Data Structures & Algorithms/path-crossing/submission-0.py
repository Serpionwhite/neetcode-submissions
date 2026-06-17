class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path_length = len(path)

        if path_length < 2:
            return False


        hash_map = {(0,0):1}

        x,y = 0,0

        for direction in path:
            if direction == 'N':
                x += 1
            elif direction == 'S':
                x -= 1

            elif direction == 'E':
                y += 1
            else:
                y -= 1

            if (x,y) in hash_map:
                return True
            else:
                hash_map[(x,y)] = 1


        return False
