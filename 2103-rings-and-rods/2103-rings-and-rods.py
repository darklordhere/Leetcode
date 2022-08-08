class Solution:
    def countPoints(self, rings: str) -> int:
        return sum(all(color + rod in rings for color in 'RGB') for rod in '0123456789')