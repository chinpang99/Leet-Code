class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        list = set()
        pointer = 0
        for i in range(0, len(s)):
            if not bool(unique) == True: # Starting
                pointer = 0
                unique.add(s[i])
                list.add(s[i])
            elif s[i] in list:
                pass
            else:
                for z in range(i+1, len(s)):
                


        for i in range(len(s)):
            if not bool(unique) == True: # Starting
                pointer = 0
                unique.add(s[i])
                list.add(s[i])
            elif s[i] not in unique:
                unique.add(s[i])
                list.add(s[i])
            elif s[i] in list:
                pass


        return 0

if __name__ == "__main__":
    solution = Solution()
    a = "pwwkew"
    result = solution.lengthOfLongestSubstring(a)


    abcccdcccccad