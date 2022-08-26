class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        all = set(itertools.permutations(str(n)))
        for per in all:
            if per[0] == '0':
                continue
            x = int(''.join(per))
            if (x and (not(x & (x - 1))) ):
                return True
        return False