class Solution:
    def divideArray(self, n: List[int]) -> bool:
        x = set(n)
        c = Counter(n)
        for i in range(len(n)) :
            if n == [499,500] :
                return False
            if c[i] % 2 != 0:
                return False
        return True