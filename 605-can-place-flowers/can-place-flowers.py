class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = 0
        zeros_count = 0

        for num in flowerbed:
            if num == 1:
                break
            left += 1
        n -= left // 2 if left < len(flowerbed) else (left + 1)// 2
        for k in range(left, len(flowerbed)):
            if flowerbed[k] == 1:
                n -= (zeros_count - 1)// 2 if (zeros_count - 1)// 2 > 0 else 0
                zeros_count = 0
            else:
                zeros_count += 1
        n -= zeros_count // 2 if (zeros_count)// 2 > 0 else 0

        return n <= 0