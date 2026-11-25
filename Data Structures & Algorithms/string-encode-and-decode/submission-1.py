class Solution:

    def encode(self, strs: List[str]) -> str:

        lengths = []
        new_str = ""
        for s in strs: 
            l = len(s)
            lengths.append(l)
            new_str += ( str(l) + ",")
        new_str = new_str + "#"

        for s in strs: 
            new_str += s
        print(new_str)

        return new_str

    def decode(self, s: str) -> List[str]:
        lengths = []
        curr = ""
        s2 = s
        for char in s: 
            print(f"char={char} ")
            if char == ',':
                lengths.append(int(curr))
                curr = ""
            elif char == "#": 
                s2 = s2[1:]
                break
            else: # char != ,
                curr = curr + char 
            print(f" curr={curr}")
            s2 = s2[1:]
        print(lengths)
        print(s2)

        results = []
        print(lengths)
        print(s2)
        counter = 0
        for l in lengths: 
            start = counter
            end = counter + l
            curr = s2[start:end]
            results.append(curr)
            counter = counter + l
        print(results)
        return results


        
        





