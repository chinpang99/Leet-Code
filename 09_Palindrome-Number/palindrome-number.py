class Solution:
    def __init__(self):
        pass
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x



if __name__ == "__main__":
    solution = Solution()
    result = solution.isPalindrome(101)
    print(result)