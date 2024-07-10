class Queen:
    def __init__(self, row, column):
        # If the row parameter is negative
        if column < 0:
            raise ValueError("column not positive")
        # If the row parameter is negative
        if row < 0:
            raise ValueError("row not positive")
        #  If the row parameter is not on the defined board
        if row not in range(8):
            raise ValueError("row not on board")
        # If the row parameter is not on the defined board
        if column not in range(8):
            raise ValueError("column not on board")
        
        
        self.row = row
        self.column = column


    def can_attack(self, another_queen):
        # If both the queens are on the same location
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        # Same row or same column or same distance in row and column
        return  abs(self.row - another_queen.row) == abs(self.column - another_queen.column) or self.row == another_queen.row or self.column == another_queen.column