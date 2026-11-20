class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nRows = len(board)
        nCols = len(board[0])
        path = []
        def dfs(i,j,k, curr): 
            if curr == word: 
                return True
            if i < 0 or j < 0 or i >= nRows or j >= nCols:
                return False 
            if board[i][j] != word[k]: 
                return False 
            if [i,j] in path: 
                return False
            
            path.append([i,j])
            curr += word[k]
            results = (dfs(i+1,j,k+1,curr) or 
                        dfs(i-1,j,k+1,curr) or 
                        dfs(i,j+1,k+1,curr) or 
                        dfs(i,j-1,k+1,curr))
            path.pop()
            curr = curr[:-1]
            return results

        for i in range(nRows):
            for j in range(nCols):
                if dfs(i,j,0,""): 
                    return True
        return False 
