class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        return t in sum(m,[]) #1
        # return any([t in i for i in m]) #2
        #3
        # for i in m:
        #     if t in i:
        #         return True
        # return False
