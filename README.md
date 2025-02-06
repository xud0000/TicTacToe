# 圈圈叉叉 (Tic-Tac-Toe)

這是一個用 Python 和 Tkinter 實現的圈圈叉叉遊戲。玩家可以和電腦進行對戰，遊戲中包含了簡單的 Minimax 演算法，讓電腦能夠根據當前棋盤狀況自動選擇最佳步驟。

This is a Tic-Tac-Toe game implemented using Python and Tkinter. Players can compete against the computer, and the game features a simple Minimax algorithm that allows the computer to automatically select the best move based on the current board state.

## 特點 (Features)

- **玩家與電腦對戰 (Player vs. Computer)**: 玩家與電腦輪流下棋，電腦使用 Minimax 演算法來選擇最佳步驟。  
  Players take turns playing against the computer, which uses the Minimax algorithm to make optimal moves.
- **遊戲狀態顯示 (Game Status Display)**: 顯示當前是玩家 X 還是玩家 O 的回合，並在遊戲結束時顯示勝利者或平手結果。  
  The game shows whose turn it is (Player X or Player O), and displays the winner or a draw message when the game ends.
- **重新開始功能 (Restart Functionality)**: 當遊戲結束後，可以點擊 "重新開始" 按鈕，重新開始一局新的遊戲。  
  After the game ends, players can click the "Restart" button to start a new game.

## 遊戲規則 (Game Rules)

- 玩家輪流在 3x3 的棋盤上放置 X 或 O。  
  Players take turns placing X or O on a 3x3 board.
- 如果任一方在水平方向、垂直方向或對角線上排成一行，則該方獲勝。  
  The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
- 若棋盤填滿且無人獲勝，則為平手。  
  If the board is filled without a winner, the game results in a draw.

## 如何運行 (How to Run)

1. 克隆或下載專案。  
   Clone or download the project.
2. 安裝 Python 3.x 和 Tkinter（通常 Tkinter 已經隨 Python 安裝）。  
   Install Python 3.x and Tkinter (Tkinter is usually included with Python).
3. 執行 `ooxxOK.py` 開始遊戲。  
   Run `ooxxOK.py` to start the game.

```bash
python ooxxOK.py
