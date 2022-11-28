class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        w = [] ; l = []
        dp=defaultdict(int)

        for i in m:
            dp[i[1]]+=1
        for i in m:
            if i[0] not in dp: #O(1)
                w.append(i[0])
                
        for i in m:
            if dp[i[1]]==1:
                l.append(i[1])
        
        return [sorted(set(w)),sorted(set(l))]