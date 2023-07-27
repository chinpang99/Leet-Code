class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            start_point = 0
            end_point = 1
        else:
            result = {}
            for i in range(0, len(s)):
                list = set()
                list.add(s[i])
                
                for z in range(i+1, len(s)):
                    if s[z] not in list:
                        list.add(s[z])
                        result[i] = z-i+1 # Store the index in dict
                    elif z == (len(s)-1) and result == {}:
                        result[i] = z-i # Store the index in dict
                    else:
                        break
            
            biggest, start_point, end_point = -1, -1, -1
            for key, value in result.items(): #Find the longest substring length
                if biggest == -1:
                    biggest = value
                    start_point, end_point = key, key+value
                elif biggest < value:
                    biggest = value
                    start_point, end_point = key, key+value 

        final_result = len(s[start_point:end_point])
        final_result = 1 if len(s) == 1 else final_result
        print("The result is {}, with the length of {}.".format(s[start_point:end_point], final_result))
        return final_result

if __name__ == "__main__":
    solution = Solution()
    a = "aab"
    result = solution.lengthOfLongestSubstring(a)