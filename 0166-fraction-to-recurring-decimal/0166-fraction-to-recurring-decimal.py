class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if numerator*denominator<0:
            res+='-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        res+= str(numerator//denominator)
        carrier = numerator%denominator
        if carrier>0:
            res+='.'
        memo = {}
        while carrier>0:
            if carrier in memo:
                index = memo[carrier]
                res = res[:index]+'('+res[index:] +')'
                return res
            else:
                memo[carrier]=len(res)
                res+=str((carrier*10)//denominator)
                carrier = ((carrier*10)%denominator)
        return res