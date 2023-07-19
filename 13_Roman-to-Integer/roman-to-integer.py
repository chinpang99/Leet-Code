class Solution:
    def __init__(self):
        pass

    def romanToInt(self, s: str) -> int:
        romanSymbol = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500,
            "M": 1000
        }
        
        value = 0
        check = False
        for i in range(len(s)):
            if check:
                check = False
                continue
            if (i+1) == len(s):
                value+=romanSymbol.get(s[i])
                continue
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X") :
                value = value + (romanSymbol.get(s[i+1]) - romanSymbol.get(s[i]))
                check = True
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                value = value + (romanSymbol.get(s[i+1]) - romanSymbol.get(s[i]))
                check = True
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                value = value + (romanSymbol.get(s[i+1]) - romanSymbol.get(s[i]))
                check = True
            else:
                value+=romanSymbol.get(s[i])
        
        return value
    
    ## Another Solution:
    def romanToInt_2(self, s: str) -> int:
        m = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500,
            "M": 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "III"
    result = solution.romanToInt(s)
