
import pygame
from engine import Engine
from mouse import Mouse

class Board:

    def __init__(self, window):

        self.window = window
        # board represented by 3x3 list
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # Keep track of player turn
        self.turn = {"X": True, "O": False}
        # winner of the game
        self.winner = None
        # length of segments in the 3x3 grid (values in DrawBackground())
        self.x_sec, self.y_sec = 0, 0
        # Engine
        self.engine = Engine(self)
        # Mouse
        self.mouse = Mouse()

    def drawBackground(self):

        wnd_wid = self.window.get_width()
        wnd_hei = self.window.get_height()

        self.x_sec = wnd_wid / 3
        self.y_sec = wnd_hei / 3

        self.window.fill((23, 40, 40))
        pygame.draw.line(self.window, "white", (0, self.y_sec), (wnd_wid, self.y_sec))
        pygame.draw.line(self.window, "white", (0, self.y_sec * 2), (wnd_wid, self.y_sec * 2))
        pygame.draw.line(self.window, "white", (self.x_sec, 0), (self.x_sec, wnd_hei))
        pygame.draw.line(self.window, "white", (self.x_sec * 2, 0), (self.x_sec * 2, wnd_hei))

    def drawPosition(self):

        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square == "X":
                    self.drawX((j, i))
                elif square == "O":
                    self.drawO((j, i))

    def drawX(self, coords):

        offset = 20  # reducing length to make it look nice

        startx1, starty1 = (coords[0] * self.x_sec), (coords[1] * self.y_sec)
        endx1, endy1 = (startx1 + self.x_sec), (starty1 + self.y_sec)

        startx2, starty2 = (startx1 + self.x_sec), starty1
        endx2, endy2 = (startx2 - self.x_sec), (starty2 + self.y_sec)

        pygame.draw.line(self.window, "red",
            (startx1 + offset, starty1 + offset),
            (endx1 - offset, endy1 - offset),
            15,)
        pygame.draw.line( self.window, "red",
            (startx2 - offset, starty2 + offset),
            (endx2 + offset, endy2 - offset),
            15,)

    def drawO(self, coords):

        centerx = coords[0] * self.x_sec + (self.x_sec / 2)
        centery = coords[1] * self.y_sec + (self.y_sec / 2)

        pygame.draw.circle(self.window, "blue", (centerx, centery), self.x_sec / 2 - 10, 10)

    def playHuman(self):

        if self.mouse.leftButtonReleased():

            mouse_coords = self.mouse.getMouseCoords()
            clicked_square = self.getBoardCoords(mouse_coords)

            if self.board[clicked_square[1]][clicked_square[0]] != " ":
                return

            if self.turn["X"]:
                self.board[clicked_square[1]][clicked_square[0]] = "X"
                self.turn["X"] = False
                self.turn["O"] = True

            elif self.turn["O"]:
                self.board[clicked_square[1]][clicked_square[0]] = "O"
                self.turn["X"] = True
                
                self.turn["O"] = False

    def playEngine(self):

        if self.turn["X"]:
            self.playHuman()
            return

        if self.turn["O"]:
            move = self.engine.bestMove(self.board)
            self.board[move[0]][move[1]] = "O"
            self.turn["X"] = True
            self.turn["O"] = False
            return

    def checkWinner(self, player, board):

        # horizontal checks
        for row in board:
            if all(ele == player for ele in row):
                return True

        # vertical checks
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # left-right diagonal check
        if all(board[i][i] == player for i in range(3)):
            return True

        # right-left diagonal check
        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def checkDraw(self, board):

        for row in board:
            if " " in row:
                return False

        if self.checkWinner("X", board):
            return False
        if self.checkWinner("O", board):
            return False

        return True

    def getBoardCoords(self, mouse_coords):

        clicked_square = [-1, -1]

        if mouse_coords[0] < self.x_sec:
            clicked_square[0] = 0
        elif mouse_coords[0] < self.x_sec * 2:
            clicked_square[0] = 1
        elif mouse_coords[0] < self.y_sec * 3:
            clicked_square[0] = 2

        if mouse_coords[1] < self.y_sec:
            clicked_square[1] = 0
        elif mouse_coords[1] < self.y_sec * 2:
            clicked_square[1] = 1
        elif mouse_coords[1] < self.y_sec * 3:
            clicked_square[1] = 2

        return clicked_square

    def reset(self):

        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = {"X": True, "O": False}
        self.winner = None
