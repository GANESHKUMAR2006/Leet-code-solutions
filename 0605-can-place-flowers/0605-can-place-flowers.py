class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zero_count=flowerbed.count(0)
        ones_count=flowerbed.count(1)
        total=zero_count-ones_count
        return total>=n