class Solution:
    def binarySearch(self, arr: List[int], x: int, left: int, right: int) -> int: 
        start = left
        end = right - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            if arr[mid] > x:
                end = mid - 1

            else:
                start = mid + 1

        return start




    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binarySearch(arr,x, 0, len(arr))

        right = index
        left = right - 1

        res = []

        while k!= 0:
            if left < 0:
                res.append(arr[right])
                right += 1

            elif right >= len(arr):
                res.append(arr[left])
                left -= 1

            elif x - arr[left] <= arr[right] - x:
                res.append(arr[left])
                left -= 1

            else:
                res.append(arr[right])
                right += 1

            k-= 1

        return sorted(res)

        