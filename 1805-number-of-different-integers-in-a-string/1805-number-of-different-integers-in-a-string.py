class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        rw,r = ' ',''
        for i in word:
            if i.isdigit():
                r += i
            else:
                r += rw
        return len(set(map(int, r.split())))
    
    