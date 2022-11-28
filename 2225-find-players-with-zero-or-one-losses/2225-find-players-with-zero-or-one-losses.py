class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        w = defaultdict(int) ; l = defaultdict(int) ; p = [] ; q = []
        for i in range(len(m)):
            w[m[i][0]]+=1
            l[m[i][1]]+=1
        m = max(max(w),max(l))
        for i in range(m+1):
            if ( i not in l ) and ( i in w ):
                p.append(i)
            if l[i] == 1:
                q.append(i)
        return [p,q]