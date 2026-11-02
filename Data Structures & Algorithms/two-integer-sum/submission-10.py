class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index1, value in enumerate(nums):
            dict[value] = index1
        # print(dict)

        for i, value in enumerate(nums):
            diff = target - value 
            
            if diff in dict: 
                index2 = dict[diff]
                index1 = i

                if index2 != index1:
                    return [i, index2] 

        
                 
            