class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if j > i and prices[j] <= prices[i]:
                    l.append(prices[i]-prices[j])
                    break
            else:
                l.append(prices[i])
        return l