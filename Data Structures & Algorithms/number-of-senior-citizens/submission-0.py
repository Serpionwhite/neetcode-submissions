class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            age = person[-4:][:2]

            if int(age) > 60:
                count += 1

        return count
        