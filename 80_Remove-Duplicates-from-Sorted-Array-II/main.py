from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        final_list=[]
        count=0
        nums.sort()
        for item in nums:
            if item in final_list:
                if count<1:
                    final_list.append(item)
                    count+=1
            else:
                final_list.append(item)
                count=0
        print(final_list)
        return len(final_list)

                 
if __name__ == "__main__":
    list1=[0,0,1,1,1,1,2,3,3]
    solution=Solution().removeDuplicates(list1)
    print(solution)



# Leet Code answer:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j