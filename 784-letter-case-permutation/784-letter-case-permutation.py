class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l = []
        for i in s:
            l.append(set([i.lower(),i.upper()]))
        return map("".join,itertools.product(*l))