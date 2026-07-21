class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # 1. Linii
        for rand in board:
            vazute = set()
            for valoare in rand:
                if valoare == ".": continue
                if valoare in vazute:
                    return False
                vazute.add(valoare)

        # 2. Coloane
        for coloana in zip(*board):
            vazute = set()
            for valoare in coloana:
                if valoare == ".": continue
                if valoare in vazute:
                    return False
                vazute.add(valoare)

        # 3. Pătrate
        patrate = {}
        for r in range(9):
            for c in range(9):
                valoare = board[r][c]
                if valoare == ".": continue
                
                adresa = (r // 3, c // 3)
                
                if adresa not in patrate:
                    patrate[adresa] = set()
                    
                if valoare in patrate[adresa]: 
                    return False
                    
                patrate[adresa].add(valoare)
                
        return True