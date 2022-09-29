class Solution(object):
    def findClosestElements(self, arr, k, x):
        def sortarray(num):
            return (abs(num-x),num)
        arr.sort(key=sortarray)
        returnarray = arr[:k]
        return sorted(returnarray)