class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        o,c = operations , 0
        for i in o:
            if i == "++X" or i == "X++":
                c += 1
            else:
                c-=1
        return c
        