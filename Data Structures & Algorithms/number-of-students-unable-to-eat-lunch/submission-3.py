class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        hash_map = {}

        for index in range(len(students)):
            hash_map[students[index]] = hash_map.get(students[index], 0) + 1

        result = len(students)
        for index in range(len(students)):
            if sandwiches[index] in hash_map:
                if hash_map[sandwiches[index]] != 0:
                    hash_map[sandwiches[index]] -= 1
                    result -= 1
                else:
                    return result
            else:
                return result

        return result







        