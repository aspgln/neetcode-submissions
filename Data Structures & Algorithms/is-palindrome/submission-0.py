class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = []
        for char in s: 
            if char.isalnum():
                ss.append(char)
            else: 
                pass


        length = len(ss)
        # print(length)
        for i in range(round(length/2)):

            # print(f"i = {i}, ss[i] = {ss[i]}")
            # print(f"len-i = {length-i}, s[len-i] = {ss[length-i-1]} ")
            if ss[i].casefold() == ss[length-i-1].casefold():
                pass
            else: 
                return False
        return True
