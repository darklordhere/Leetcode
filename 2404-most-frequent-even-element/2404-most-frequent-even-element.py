class Solution:
    def mostFrequentEven(self, n: List[int]) -> int:
        return mode(sorted(x for x in n if not x % 2) + [-1])