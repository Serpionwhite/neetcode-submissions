class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        array_length = len(arr)
        result = [0] * array_length
        if array_length < 2:
            return [-1]

        result[-1] = -1
        max_value = arr[-1]

        for index in range(array_length-2,-1,-1):
            result[index] = max_value
            max_value = max(arr[index], max_value)


        return result
        