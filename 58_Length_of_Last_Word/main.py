class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    word1='Hello World'
    solution = Solution().lengthOfLastWord(word1)
    print(solution)

