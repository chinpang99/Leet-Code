from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = set()
        count = 0
        for item in nums:
            if item not in result:
                count+=1
                result.add(item)
        return count
        

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,2]
    result = solution.removeDuplicates(nums)
    print(result)