class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        arr1 = []
        arr2=[]
        for word in s:
            arr1.append(s.index(word))
        for word in t:
            arr2.append(t.index(word))
        if arr1==arr2:
            return True
        return False

if __name__ == "__main__":
    str1 = 'egg'
    str2='add'
    solution=Solution().isIsomorphic(str1, str2)
