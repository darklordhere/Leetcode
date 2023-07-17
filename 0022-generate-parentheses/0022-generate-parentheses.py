class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []
        def fun(l,r,s):
            if len(s) == n*2:
                rs.append(s)
                return
            if l < n:
                fun(l+1,r,s+"(")
            if r < l:
                fun(l,r+1,s+")")
        fun(0,0,"")
        return rs
        