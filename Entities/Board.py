class Board:
    def __init__(self):
        self.row = []
        self.board = []

    def construct(self, stack, objectsinstack=None):
        if objectsinstack is None:
            objectsinstack = []
        for i in range(stack):
            self.board.append(['*'])
        for i in range(len(self.board)):
            for j in range(objectsinstack[i]-1):
                self.board[i].append('*')
        self.row = objectsinstack

