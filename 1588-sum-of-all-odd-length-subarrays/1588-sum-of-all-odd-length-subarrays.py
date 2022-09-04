class Solution:
    def sumOddLengthSubarrays(self, a: List[int]) -> int:
        s = sum(a)
        for i in range(3,len(a)+1,2):
            for j in range(len(a)):
                if i+j > len(a):
                    break
                s += sum(a[j:j+i])
        return s