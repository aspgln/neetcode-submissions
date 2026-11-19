class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        low = 0
        high = 1
        profit = 0 

        while curr < len(prices): 
            if prices[curr] <= prices[low]: 
                low = curr 
             
            if prices[curr] - prices[low] >= profit: 
                high = curr
                profit = prices[high] - prices[low]
            curr += 1 
        return profit  
                
    