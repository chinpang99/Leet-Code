class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = [ele for ele in nums if ele != val]
        print(nums)
        return len(nums)

if __name__ == "__main__":
    solution=Solution()
    list1 = [0,1,2,2,3,0,4,2]
    val = 2
    solution2=solution.removeElement(list1, val)
    print(solution2)