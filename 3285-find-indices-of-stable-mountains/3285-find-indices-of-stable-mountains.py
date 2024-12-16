class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        c = []
        for i in range(1,len(height)):
            if height[i-1] > threshold:
                c.append(i)
        return c