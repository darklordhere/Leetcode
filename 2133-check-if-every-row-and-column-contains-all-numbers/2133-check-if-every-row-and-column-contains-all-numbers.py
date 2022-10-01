class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(set(row)) == len(matrix) for row in matrix) and all(len(set(col)) == len(matrix) for col in zip(*matrix))