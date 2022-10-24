class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return len(max(reduce(lambda x,y: x+[i+y for i in x if len(i+y)==len(set(i+y))], arr, ['']), key= lambda x: len(x)))