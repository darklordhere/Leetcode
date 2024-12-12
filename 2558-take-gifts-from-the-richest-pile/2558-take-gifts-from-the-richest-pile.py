class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k != 0:
            gifts = sorted(gifts)[::-1]
            gifts[0] = int(math.sqrt(gifts[0]))
            k -= 1
        return sum(gifts)