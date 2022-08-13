class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tr = 'abcdefghijklmnopqrstuvwxyz0'
        trs = 'abcdefghijklmnopqrstuvwxyz'
        rw = ' '
        r = ''
        for i in word:
            if i.isdigit():
                r += i
            else:
                r += rw
        x = r.split()
        print(r)
        return len(set(map(int, r.split())))
    
    