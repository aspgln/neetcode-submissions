class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        maxf = 0
        maxL = 0
        counter = {}

        for r, char in enumerate(s):
            # print("curr_str")
            if char not in counter:
                counter[char] = 0 
            else: 
                counter[char] += 1

            maxf = max(counter.values())+1

            if r-left+1 - maxf >  k:
                counter[s[left]] -= 1 
                left = left + 1

            maxL = max(maxL, r-left+1)
            # print(f"left{left}, right={r}, wind={r-left+1}, maxf={maxf}, tol={r-left-maxf+1}, maxL={maxL}, counter={counter}")
        return maxL


