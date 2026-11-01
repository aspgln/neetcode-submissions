class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] not in dict1: 
                dict1[s[i]] = 0
            elif s[i] in dict1: 
                dict1[s[i]] += 1
            
            if t[i] not in dict2: 
                dict2[t[i]] = 0
            elif t[i] in dict2: 
                dict2[t[i]] += 1

           
        return dict1 == dict2

