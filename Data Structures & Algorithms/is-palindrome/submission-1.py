class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s: 
            if char.isalnum():
                newStr += char.lower()
        print(s)
        print(newStr)

        for i in range(len(newStr)): 
            if newStr[i] == newStr[len(newStr)-i-1]:
                pass
            else: 
                return False

        return True