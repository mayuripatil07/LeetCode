class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while(i < len(flowerbed)):
            if flowerbed[i] == 0 :
                if i + 1 == len(flowerbed):
                    n -= 1
                    i += 2
                elif i + 1 < len(flowerbed) and flowerbed[i+1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1

            elif flowerbed[i] == 1:
                i += 2
        if n > 0:
            return False
        return True
            
