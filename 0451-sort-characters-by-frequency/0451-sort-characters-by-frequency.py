class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(x*y for x,y in Counter(s).most_common())