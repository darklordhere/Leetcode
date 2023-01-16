class Solution:
    def singleNonDuplicate(self, n: List[int]) -> int:
        for i,j in Counter(n).items():
            if j == 1:
                return i