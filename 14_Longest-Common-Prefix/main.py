from typing import List

class Solution:
    def __init__(self) -> None:
        pass
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]
        return base 


if __name__ == "__main__":
    solution = Solution()
    list = ["flower","flow","flight"]
    result = solution.longestCommonPrefix(list)
    print("Result: " + result)