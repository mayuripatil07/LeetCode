class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = [""]
        for d in digits:
            res = []
            for char in m[d]:
                for r in result:
                    res.append(r + char)
            result = res
        return result
                
