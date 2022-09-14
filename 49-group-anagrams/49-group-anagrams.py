class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for j in s:
            c = [0]*26
            for i in j:
                c[ord(i) - ord("a")] += 1
            x[tuple(c)].append(j)
        return x.values()