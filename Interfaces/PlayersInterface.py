from abc import ABC


class Players(ABC):
    def __init__(self):
        self.gamesWon: int = 0
