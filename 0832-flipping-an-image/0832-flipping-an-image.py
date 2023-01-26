class Solution:
    def flipAndInvertImage(self, i: List[List[int]]) -> List[List[int]]:
        for j in range(len(i)):
            i[j] = i[j][::-1]
            for k in range(len(i)):
                if i[j][k] == 0: i[j][k] = 1
                else: i[j][k] = 0
        return i
            