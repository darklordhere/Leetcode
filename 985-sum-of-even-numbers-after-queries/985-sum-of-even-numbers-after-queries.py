class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans, curr = [], sum(n for n in A if n % 2 == 0)
        for val, idx in queries:
            prev = A[idx]
            A[idx] += val
            if prev % 2 == 0:
                curr -= prev
            if A[idx] % 2 == 0:
                curr += A[idx]
            ans.append(curr)
        return ans

        