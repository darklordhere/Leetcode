class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=nums[0:len(nums)//2]
        b=nums[len(nums)//2:]
        
        res=[]
        for i,y in zip(a,b):
            res.append(i)
            res.append(y)
        return res