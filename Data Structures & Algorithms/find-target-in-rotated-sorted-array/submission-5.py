class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # step 1: find the inflection point and split into two array
        # step 2: find val in each 

        l = 0
        r = len(nums)-1 
        pivot = l

        while l < r:
            if nums[l] <= nums[r]: 
                pivot = l 
                break
            mid = (l+r)//2 
            if nums[mid] <= nums[r]: 
                r = mid 
            else: 
                l = mid + 1 
        pivot = l 
        print(f"pivot={pivot}, val = {nums[pivot]}")

        nums_left = nums[:pivot]
        nums_right = nums[pivot:]
        print(nums_left)
        print(nums_right)

        def binary_search(array, target):
            l = 0
            r = len(array)-1

            if not len(array):
                return -1 
                
            if target > array[-1] or target < array[0]:
                return -1

            while l <= r: 
                mid = (l+r)//2 

                if array[mid] == target: 
                    return mid 
                elif array[mid] < target: 
                    l = mid + 1 
                else: 
                    r = mid - 1 
            return -1 

        out1 = binary_search(nums_left, target)
        print(f"out1 = {out1}")

        if out1 != -1: 
            return out1
        else: 
            out2 = binary_search(nums_right, target)
            print(f"nums_right = {nums_right},out2 = {out2}")

            if out2 == -1: 
                return -1 
            else:
                return out2 + pivot 





