from Entities.Players import HumanPlayer, AutomaticPlayer
from Interfaces.PlayersInterface import Players
from Entities.Tree import GeneralTree


class MiniMaxAlgorithm:
    def __init__(self):
        self.generalTree = GeneralTree()
    @staticmethod
    def winner(row):
        for i in range(len(row)):
            if row[i] != 0:
                return False
        return True

    def possiblemovements(self, row):
        self.generalTree.add_child(parent=None, child=row)
        for i, columns in enumerate(row):
            new_row = row
            for j in range(0, columns):
                new_row[i] -= j


    def minimax(self, row, player: Players):
        if self.winner(row):
            if type(player) is HumanPlayer:
                return -1
            elif type(player) is AutomaticPlayer:
                return 1
        bestgame = -999
        if type(player) is HumanPlayer:
            for move in self.possiblemovements(row):
                value = self.minimax(move, player)
                if bestgame < value:
                    bestgame = value
        elif type(player) is AutomaticPlayer:
            for move in self.possiblemovements(row):
                value = self.minimax(move, player)
                if bestgame >= value:
                    bestgame = value
        return bestgame


mma = MiniMaxAlgorithm()

p1 = AutomaticPlayer()
print(mma.minimax([1,2,3], p1))
