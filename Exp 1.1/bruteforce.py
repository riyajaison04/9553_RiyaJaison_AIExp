
import sys

EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 3

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = PLAYER_X

    def initialize_board(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.board[i][j] = EMPTY

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_board_full(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def has_won(self, player):
        # Check rows and columns
        for i in range(BOARD_SIZE):
            if all(self.board[i][j] == player for j in range(BOARD_SIZE)) or \
               all(self.board[j][i] == player for j in range(BOARD_SIZE)):
                return True
        # Check diagonals
        return (all(self.board[i][i] == player for i in range(BOARD_SIZE)) or
                all(self.board[i][BOARD_SIZE-i-1] == player for i in range(BOARD_SIZE)))

    def is_valid_move(self, row, col):
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and self.board[row][col] == EMPTY

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def evaluate(self):
        if self.has_won(PLAYER_X):
            return 1
        elif self.has_won(PLAYER_O):
            return -1
        else:
            return 0

    def minimax(self, depth, is_maximizing):
        score = self.evaluate()

        # Base case: terminal state reached
        if score != 0:
            return score

        # If it's AI's turn
        if is_maximizing:
            best_score = float('-inf')
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = PLAYER_X
                        current_score = self.minimax(depth + 1, False)
                        self.board[i][j] = EMPTY
                        best_score = max(best_score, current_score)
            return best_score
        else:  # If it's human's turn
            best_score = float('inf')
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = PLAYER_O
                        current_score = self.minimax(depth + 1, True)
                        self.board[i][j] = EMPTY
                        best_score = min(best_score, current_score)
            return best_score

    def ai_move(self):
        best_score = float('-inf')
        best_row, best_col = -1, -1

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_X
                    current_score = self.minimax(0, False)
                    self.board[i][j] = EMPTY
                    if current_score > best_score:
                        best_score = current_score
                        best_row, best_col = i, j

        self.make_move(best_row, best_col, PLAYER_X)

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("You are playing against the unbeatable AI.")

        while not self.is_board_full() and not self.has_won(PLAYER_X) and not self.has_won(PLAYER_O):
            if self.current_player == PLAYER_X:
                self.ai_move()
            else:
                print("Your move (row column): ")
                
                row, col = map(int, input().split())
                if not self.is_valid_move(row, col):
                    print("Invalid move! Try again.")
                    continue
                self.make_move(row, col, PLAYER_O)
            self.print_board()
            self.switch_player()

        if self.has_won(PLAYER_X):
            print("AI wins! Better luck next time.")
        elif self.has_won(PLAYER_O):
            print("Congratulations! You win!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
