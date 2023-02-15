class Solution:
    def addToArrayForm(self, n: List[int], k: int) -> List[int]:
        return [int(i) for i in list(str(int("".join([str(i) for i in n]))+k))]