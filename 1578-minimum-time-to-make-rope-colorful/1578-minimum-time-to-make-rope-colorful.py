class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = sumSameColor = maxSameColor = 0
        for index in range(len(colors)):
            if index > 0 and colors[index] != colors[index - 1]:
                result += (sumSameColor - maxSameColor)
                maxSameColor = sumSameColor = neededTime[index]
            else:
                sumSameColor += neededTime[index]
                maxSameColor = max(neededTime[index], maxSameColor)
        result += (sumSameColor - maxSameColor)
        return result