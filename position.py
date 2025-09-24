class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


    def move_down(self):
        self.row += 1

    def move_left(self):
        self.column -= 1

    def move_right(self):
        self.column += 1


    