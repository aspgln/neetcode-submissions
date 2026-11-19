class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0: 
            return 0 

        l = 0
        maxL = 1
        dict={}

        for i, char in enumerate(s):
            # print(f"before: l={l}={s[l]}, r={i}={char},maxL={maxL}")
            if char in dict: 
                l = max(dict[char] + 1 , l)
            # print(dict)

            dict[char] = i
            maxL = max(maxL, i-l+1)
            # print(f"after : l={l}={s[l]}, r={i}={s[i]},maxL={maxL}")
        return maxL


        


        # for i, char in enumerate(s): 
        #     print(f"before: l={l}={s[l]}, r={r}={s[r]},maxL={maxL}")
        #     if char not in dict: 
        #         dict[char] = i
        #         maxL = max(maxL, r-l+1)  
        #         r = r+1

        #     if char in dict: 
        #         l = dict[char] + 1
        #         r = r + 1 
        #         dict[char] = i

        #     print("    ")

            
        # return maxL 
