
class Engine:

    def __init__(self, board):

        self.board = board

    def bestMove(self, board):

        best_move = (-1, -1)
        score, best_score = 0, float("-inf")

        for row, i in enumerate(board):
            for col, j in enumerate(i):
                if j == " ":
                    board[row][col] = "O"
                    score = self.minMax(board, False)
                    board[row][col] = " "

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minMax(self, board, isMaxing):

        if self.board.checkWinner("X", board):
            score = -1
            return score

        if self.board.checkWinner("O", board):
            score = 1
            return score

        if self.board.checkDraw(board):
            score = 0
            return score

        if isMaxing:
            best_score = float("-inf")

            for row, i in enumerate(board):
                for col, j in enumerate(i):
                    if j == " ":
                        board[row][col] = "O"
                        score = self.minMax(board, False)
                        board[row][col] = " "

                        if score > best_score:
                            best_score = score

            return best_score

        else:
            best_score = float("inf")

            for row, i in enumerate(board):
                for col, j in enumerate(i):
                    if j == " ":
                        board[row][col] = "X"
                        score = self.minMax(board, True)
                        board[row][col] = " "

                        if score < best_score:
                            best_score = score

            return best_score
