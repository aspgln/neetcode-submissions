class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nRows = len(board)
        nCols = len(board[0])
        previous_path = []

        def dfs(i,j, k):
            # i,j, index 
            # k: current idnex in word 
            if k == len(word): 
                return True
            # curr_char = board[i][j]

            if i < 0 or j < 0 or i >= nRows or j >= nCols or [i,j] in previous_path or k >= len(word) or board[i][j] != word[k]:
                return False 

            previous_path.append([i,j])
            results = (dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1))
            previous_path.pop()
            return results


        
        for i in range(nRows):
            for j in range(nCols):
                ans = dfs(i,j,0)
                if ans: 
                    return True
        return False 
                
