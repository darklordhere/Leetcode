class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        return t in sum(m,[])
        # return any([t in i for i in m])
        # for i in m:
        #     if t in i:
        #         return True
        # return False
