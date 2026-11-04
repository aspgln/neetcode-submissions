class Solution:
    # this solution uses reversing a new string 
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s: 
            if char.isalnum():
                newStr += char.lower()
        print(s)
        print(newStr)

        for i in range(round(len(newStr)/2)): 
            if newStr[i] == newStr[len(newStr)-i-1]:
                pass
            else: 
                return False

        return True