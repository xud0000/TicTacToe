
import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("圈圈叉叉")

        self.buttons = []
        self.turn = "X"
        self.board = [""] * 9

        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text="", width=10, height=3, font=("Helvetica", 24),
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        self.turn_label = tk.Label(root, text="輪到X了", font=("Helvetica", 16))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.restart_button = tk.Button(root, text="重新開始", command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        self.reset_board()

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.turn = "X"
        self.turn_label.config(text="輪到X了")

    def restart_game(self):
        self.reset_board()
        self.turn = random.choice(["X", "O"])
        if self.turn == "O":
            self.computer_move()

    def make_move(self, row, col):  #玩家移動
        index = 3 * row + col
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_winner():
                messagebox.showinfo("遊戲結束", f"玩家{self.turn} 獲得勝利")
                self.restart_game()
            elif "" not in self.board:
                messagebox.showinfo("平手", "平手")
                self.restart_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.turn_label.config(text=f"輪到玩家 {self.turn}")
                if self.turn == "O":
                    self.computer_move()

    def computer_move(self):  #電腦移動
        if not self.check_winner():
            index = self.get_best_move()
            self.make_move(index // 3, index % 3)

    def get_best_move(self):  #尋找最佳位置
        best_move = None
        best_score = -float("inf")
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing): #minimax演算法
        winner = self.check_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif "" not in board:
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                return self.board[line[0]]
        return ""
    """
    0 1 2
    3 4 5
    6 7 8
    """

root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()
