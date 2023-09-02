class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        x = [0]*n
        a = 1 ; b = 0 ; z = 0
        while b < n:
            for i in x:
                if i+a == k:
                    if a == k:
                        pass
                    else:
                        a += 1
                        break
            else:
                x[z] = a
                a += 1;z += 1;b += 1
        return sum(x)
            