class Solution:
    def bestClosingTime(self, customers: str) -> int:
        x = y = z = 0
        for i, charr in enumerate(customers):     
            z += (charr == "Y") * 2 - 1       
            if z > y:                       
                y, x = z, i+1               
        return x