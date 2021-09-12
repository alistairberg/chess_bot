import chess

class Game:
    """Class to manage game play"""

    def __init__(self):
        """Initialize game of chess"""
    board = chess.Board()
    print(board)        

if __name__ == '__main__':
    chess = Game()