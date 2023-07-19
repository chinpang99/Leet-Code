from typing import List

class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                   return [i,j]
        return []

    def twoSum_HastTable(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)        