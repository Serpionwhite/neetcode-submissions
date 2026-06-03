class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n== 0:
            return True

        bed_size = len(flowerbed)

        if (bed_size <2 and n > 1):
            return False

        # if bed_size == 2 and n==1:
        #     if bed_size[0] != 0  or bed_size[1] != 0:
        #         return False

        #     if bed_size[0] == 0 and bed_size[1] == 0:
        #         return True


        for index in range(bed_size):
            if flowerbed[index] == 0:
                if (index == 0 or flowerbed[index-1] == 0) and (index == bed_size - 1 or flowerbed[index+1] == 0):
                    flowerbed[index] = 1
                    n-= 1
            
            if n==0:
                break


        if n!= 0:
            return False
        return True


        

        