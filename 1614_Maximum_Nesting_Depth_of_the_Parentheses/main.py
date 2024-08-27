class Solution:
    def maxDepth(self, s: str) -> int:
        return max([s[:i].count('(') - s[:i].count(')') for i in range(len(s) + 1)])
        

if __name__ == "__main__":
    a="8*((1*(5+6))*(8/6))"
    solution=Solution().maxDepth(a)
    print(solution)
