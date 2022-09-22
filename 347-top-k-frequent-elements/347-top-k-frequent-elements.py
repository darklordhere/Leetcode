class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        dic = {}
        for i in n:
            if i in dic: dic[i] = dic[i] +1
            else: dic[i] = 1
        return sorted(dic, key = dic.get,reverse = True)[:k]