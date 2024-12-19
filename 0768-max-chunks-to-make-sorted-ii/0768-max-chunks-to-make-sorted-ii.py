class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in arr:
            largest = i
            while stack and i < stack[-1]:
                largest = max(largest,stack.pop())
            stack.append(largest)
        return len(stack)