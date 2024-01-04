class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        l = [i.count("1") for i in b if i.count("1") > 0]
        return (sum([l[i]*l[i+1] for i in range(len(l)-1)]) if len(l)>1 else 0)