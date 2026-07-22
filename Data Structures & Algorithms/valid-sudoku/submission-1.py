class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for row in board:
            newRow = [x for x in row if x != '.']
            
            myset = list(dict.fromkeys(newRow))
            
            if len(myset) != len(newRow):
                return False
        
        # Column
        for col in range(9):
            column = []
            myColumnSet = set()
             
            for row in range(9):
                
                if board[row][col] != ".":
                    myColumnSet.add(board[row][col])
                    column.append(board[row][col])

            if len(column) !=len(myColumnSet) :
                return False

        # square check
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):

                square = []
                squareSet = set()

                for r in range(3):
                    for c in range(3):
                        value = board[row + r][column + c]
                        if value != ".":
                            
                            square.append(value)
                           
                squareSet = list(dict.fromkeys(square))
                if(square != squareSet):
                    return False
                
        return True
                
        
            

        # return res