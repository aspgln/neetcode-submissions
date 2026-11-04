class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        length = len(s)
        print(f"size of s = {length}")
        l, r = 0, length

        while l < r: 
            if not s[l].isalnum(): 
                l = l+1
            else: 
                if not s[r-1].isalnum(): 
                    r = r - 1
                else: 
                    print(f"l={l}, r={r}, s[l]={s[l]}, s[r]-1 = {s[r-1]}")

                    if s[l].lower() == s[r-1].lower():
                        l += 1
                        r -= 1 
                    else: return False 
        
        return True
