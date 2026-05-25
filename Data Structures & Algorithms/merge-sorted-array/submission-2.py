class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        start1 = m-1
        start2 = n-1
        fill_length = m+n-1

        while start1 != -1 and start2 != -1:
            if nums1[start1] > nums2[start2]:
                nums1[fill_length] = nums1[start1]
                start1 -= 1
            else:
                nums1[fill_length] = nums2[start2]
                start2 -= 1
            fill_length -= 1


        while start1 > -1:
            nums1[fill_length] = nums1[start1]
            start1 -= 1
            fill_length -= 1

        while start2 > -1:
            nums1[fill_length] = nums2[start2]
            start2 -= 1
            fill_length -=1

        