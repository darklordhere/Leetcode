class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if numRows == 1:
        #     return [[1]]
        # elif numRows > 1 and numRows < 6:
        #     r = [[1]]
        #     for i in range(1,numRows):
        #         r.append(map(int,str(11**i)))
        #     return r
        # else:
        r = []
        for i in range(1,numRows+1):
            b = 1
            t = []
            for j in range(1,i+1):
                t.append(b)
                b = b*(i-j)//j
            r.append(t)
        return r
            
        # r = []
        # for i in range(numRows):
        #     t = ""
        #     for j in range(numRows+1):
        #         t += str((factorial(i))//(factorial(abs(i-j))*factorial(j)))
        #     r.append([*map(int,str(t[:i-j]))])
        # return r
