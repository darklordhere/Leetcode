class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c = current.split(':')
        cr = correct.split(':')
        c = (int(cr[0])- int(c[0])) * 60 + ( int(cr[1])- int(c[1]))
        r = (c//60) + ((c%60)//15) + ((c%15) // 5) + (c%5)
        return r