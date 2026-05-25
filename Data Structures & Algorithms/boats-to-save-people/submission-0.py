class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        start = 0
        end = n-1

        count = 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            count +=1
            end -=1

        return count