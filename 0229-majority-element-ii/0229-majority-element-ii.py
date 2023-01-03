class Solution:
    def majorityElement(self, n: List[int]) -> List[int]:
        x = Counter(n)
        return [i for i in x if x[i]>len(n)/3]