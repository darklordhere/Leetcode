class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(b,2)+int(a,2))[2:]