class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        answer = nums[l]

        while l < r: 

            if nums[l] <= nums[r]: 
                answer = nums[l]

            mid = (l+r)//2
            print(f"l={l}, mid={mid},r={r}, nums[l,mid,r]={nums[l],nums[mid], nums[r]}")
            if nums[mid] <= nums[r]: 
                r = mid 
            else: 
                l = mid +1
            print(f"kept arry: l={l}, r={r},[{nums[l:r]}]")

        answer = nums[l]
        return answer