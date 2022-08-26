class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def isp( n: int) -> bool:
            if n <= 0:
                return False
            else:
                while n > 1:
                    n /= 2
                return n == 1
        all = set(itertools.permutations(str(n)))
        for per in all:
            if per[0] == '0':
                continue
            else:
                if (isp(int(''.join(per)))) == True :
                    return True
        return False