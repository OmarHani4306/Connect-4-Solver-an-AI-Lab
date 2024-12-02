
    def __init__(self, root, algorithm, k=None):
        self.root = root
        self.algorithm = algorithm
        self.k = k
        self.board = [[str(EMPTY) for _ in range(COLS)] for _ in range(ROWS)]
        self.top_row = [ROWS -