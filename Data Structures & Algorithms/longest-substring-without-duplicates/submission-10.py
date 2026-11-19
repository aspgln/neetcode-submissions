class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0

        left = 0
        maxL = 0
        counter = {}

        for i, char in enumerate(s):

            if char in counter: 
                left = max(counter[char]+1, left)

            counter[char] = i
            maxL = max(maxL, i-left+1)

            # print(f"l={left}, r={i}, maxL={maxL},counter={counter}")
        
        return maxL