class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for i in s: x[str((sorted(i)))].append(i)
        return x.values()