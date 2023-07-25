from typing import List

class Solution:
    def __init__(self) -> None:
        pass
    
    def isValid(self, s: str) -> bool:
        bracket:List = {"(": ")", 
                        "{": "}", 
                        "[": "]"
                    }
        for keys, value in bracket.items():
            if keys in s:
                if s.count(keys) == s.count(value):
                    pass
                else:
                    return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = "()"
    result = solution.isValid(s)