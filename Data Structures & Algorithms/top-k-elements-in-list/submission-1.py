class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            if num not in count: 
                count[num] = 0
            else: 
                count[num] += 1

        # print(count)

        top_k = sorted(count)
        top_k = sorted(count, key = count.get, reverse=True)

        # print(top_k)
        return top_k[:k]