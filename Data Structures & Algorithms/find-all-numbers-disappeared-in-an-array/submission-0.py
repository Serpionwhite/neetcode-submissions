class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        total_number = len(nums)
        result = []
        number_marker = [False] * (total_number + 1)

        for index in range(total_number):
                number_marker[nums[index]] = True
        
        for index in range(1,total_number+1):
            if number_marker[index] == False:
                result.append(index)

        return result

        