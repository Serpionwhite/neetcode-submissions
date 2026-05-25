class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if k==n or k ==0 or n <=1:
            return nums

        k = k%n

        def reverse(arr, start, end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -=1
            return arr

        nums = reverse(nums, 0,n-1)
        nums = reverse(nums,0,k-1)
        nums = reverse(nums,k,n-1)

        return nums
        