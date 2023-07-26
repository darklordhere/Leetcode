class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        x = [] ; i = 0
        while i < len(arr):
            if arr[i] == 0:
                x.append(arr[i])
                x.append(0)
            else:
                x.append(arr[i])
            i += 1
        arr[:] = x[:len(arr)]
        return arr
            
        