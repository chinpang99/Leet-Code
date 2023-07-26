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
    
    # Stack Method
    def isValid(self, s: str) -> bool:
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()
    s = "()"
    result = solution.isValid(s)