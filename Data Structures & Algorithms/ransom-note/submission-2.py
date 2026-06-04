class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mapper_ransom = collections.Counter(ransomNote)
        mapper_magazine = collections.Counter(magazine)

        for key in mapper_ransom.keys():
            if mapper_ransom[key] > mapper_magazine[key]:
                return False

        return True

