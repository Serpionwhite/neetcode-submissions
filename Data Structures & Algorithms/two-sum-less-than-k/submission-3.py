class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # max_sum = -1

        # start = 0
        # end = len(nums) - 1

        # while start < end:
        #     if nums[start] + nums[end] < k:
        #         max_sum = max(max_sum, nums[start] + nums[end])
        #         start+= 1
        #     else:
        #         end-=1

        # return max_sum

        count = [0] * 1001
        for value in nums:
            count[value] += 1

        start = 0
        end = 1000
        max_sum = -1

        while start <= end:
            total_sum = start + end
            if total_sum >= k or count[end] == 0:
                end -= 1

            else:
                if count[start] == 0:
                    start += 1
                else:
                    if (start < end) or (count[start] > 1):
                        max_sum = max(max_sum, total_sum)
                    start += 1
        return max_sum

            

        