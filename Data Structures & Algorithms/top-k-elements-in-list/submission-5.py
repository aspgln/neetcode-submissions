class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # dict: key = num, value = count
        for num in nums:
            if num not in d: 
                d[num] = 1
            else: # num in d
                d[num] += 1
        # sorted by count, return num
        # -> sorted by values, return keys
        # print(d)
        arr = sorted(d, key=d.get, reverse=True)   
        # print(arr) 
        return arr[:k]