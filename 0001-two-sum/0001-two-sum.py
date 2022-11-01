class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i in range(len(n)):
            for j in range(i):
                if n[i] + n[j] == t:
                    return [i,j]
                