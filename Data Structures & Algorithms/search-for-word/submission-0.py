class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        CURR_PATH = set()

        def dfs(i,j,curr):
            if curr == len(word): 
                return True 
            if i<0 or j<0 or i>=ROWS or j >= COLS:
                return False 
            if (i,j) in CURR_PATH: 
                return False 
            if word[curr] != board[i][j]: 
                return False 
            
            CURR_PATH.add((i,j))
            result = dfs(i+1, j, curr+1) or dfs(i-1, j, curr+1) or dfs(i, j-1, curr+1) or dfs(i, j+1, curr+1)
            CURR_PATH.remove((i,j))
            return result

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0): 
                    return True
        return False 


