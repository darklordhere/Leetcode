class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        dic = {
            "1":"","2":"abc","3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"
        }
        return list(map("".join,product(*map(dic.get,d)))) if d else []
        