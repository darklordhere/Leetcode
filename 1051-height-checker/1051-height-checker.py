class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights) ; c = 0 ; i = 0
        while i < len(heights):
            if hs[i] != heights[i]:
                c += 1
            i += 1
        return c