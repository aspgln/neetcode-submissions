class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: 
            return [] 
        output = [] 
        def dfs(i, curr, total):
            # inputs: 
            # - i: index of the current candidate 
            # - curr: current list, e.g., [2,2,3]
            # - total: current sum/total of curr 

            # logic: 
            # - binary/backtracking 
            # - no repeating 
            
            if total == target: 
                output.append(curr.copy())
                return 
            
            if total > target or i >= len(nums): # end early. 
                return 

            # before [2,2]
            candidate = nums[i] # 2 
            curr.append(candidate) 
            dfs(i, curr, total+candidate) # try [2,2,2]
            curr.pop()
            dfs(i+1, curr, total) # try [2,2,3]
        
        dfs(0, [], 0)
        return output 

            
            