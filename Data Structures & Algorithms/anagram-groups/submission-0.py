class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs: 
            word_sorted = sorted(word)
            # print(word_sorted)
            key = tuple(word_sorted)
            if key in d: 
                d[key].append(word)
            else: # key not in d: 
                d[key] = [word]
        
        output = []
        for key,item in d.items():
            output.append(item)
        return output