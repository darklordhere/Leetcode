class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        # l = []
        # for p in range(len(i)):
        #     for q in range(1,len(i)):
        #         print(i[p][0],i[p][1])
        #         if i[p][1] >= i[q][0] and i[p][0] < i[q][1]:
        #             l.append([i[p][0],i[q][1]])
        #             break
        # print(l)

        i=sorted(i)
        l=[i[0]]
        if len(i)<=1: return i
        for x  in range(1,len(i)):
            if i[x][0]<=l[-1][1]: l[-1][1] = max(i[x][1],l[-1][1])
            elif i[x] not in l: l.append(i[x])
        return l