class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        return (Counter(n1) & Counter(n2)).elements()