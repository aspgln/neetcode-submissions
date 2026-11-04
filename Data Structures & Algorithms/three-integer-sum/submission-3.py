class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this solution uses 1x for loop + two pointers 
        nums.sort()
        L = len(nums)
        output = set()

        for i in range(0,L):
            # a = nums[i]
            # if a > 0: 
            #     return output 

            # if i>0 and a == nums[i-1]:
            #     continue
            
            # two pointers 
            l = i+1
            r = L-1

            while l < r:
                sums =  nums[i] + nums[l] + nums[r]
                if sums == 0: 
                    output.add(( nums[i], nums[l], nums[r]))
                    l = l+1
                    r = r-1
                elif sums < 0: 
                    l = l+1
                elif sums > 0: 
                    r = r - 1
        output = list(output)
        return output


