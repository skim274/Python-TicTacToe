import random

class TicTacToe:
    
    def __init__(self):
        
        # Initialize the game with an empty board and default settings.
        self.board = [["-" for _ in range(3)] for _ in range(3)]
        self.player = ""
        self.computer = ""
        self.whose_turn = 0  # 0 for player, 1 for computer

    def start_game(self):
        
        # Main game loop that handles the game flow.
        print("Tic Tac Toe!")
        self.player = input("Would you like to play as 'X' or 'O'? ").upper()
        
        while self.player not in ["X", "O"]:
            self.player = input("Invalid entry. Press 'X' or 'O': ").upper()
            
        self.computer = "O" if self.player == "X" else "X"
        print(f"You selected '{self.player}'. Computer is '{self.computer}'.\nGood luck!")
        
        while not self.is_board_full():
            print()
            self.display_board()
            
            if self.whose_turn == 0:
                self.player_move()
                
                if self.check_win():
                    self.display_board()
                    print("Congratulations! You win!")
                    return
                self.switch_turn()
            else:
                self.computer_move()
                
                if self.check_win():
                    self.display_board()
                    print("Sorry, Computer wins! Please try again.")
                    return
                self.switch_turn()
        
        self.display_board()
        print("Draw!")    

    def player_move(self):
        
        # Handle player's move with proper error handling.
        while True:
            try:
                print("Your turn.")
                row = int(input("Enter Row # (1-3): ")) - 1
                
                if row not in range(3):
                    print("Invalid entry. Row must be 1, 2, or 3.")
                    continue
                
                col = int(input("Enter Column # (1-3): ")) - 1
                
                if col not in range(3):
                    print("Invalid entry. Column must be 1, 2, or 3.")
                    continue
                    
                if self.board[row][col] == "-":
                    self.board[row][col] = self.player
                    return
                else:
                    print("Position already occupied. Try again.")
            
            except ValueError:
                print("Please enter a number.")
    
    def computer_move(self):
        
        # Handle computer's move using minimax algorithm.
        print("Computer's turn.")
        
        # Use minimax for optimal play
        best_score = float('-inf')
        best_move = None
        
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "-":
                    self.board[row][col] = self.computer
                    score = self.minimax(False)
                    self.board[row][col] = "-"
                    
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        if best_move:
            self.board[best_move[0]][best_move[1]] = self.computer
        else:
            # Fallback to random move if something goes wrong
            self._random_move()
    
    def _random_move(self):
        
        # Computer fallback method for making a random move.
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            
            if self.board[row][col] == "-":
                self.board[row][col] = self.computer
                return

    def minimax(self, is_maximizing):
        
        # Minimax algorithm for computer AI decision making.
        # Check for win states.
        if self.check_win_for(self.computer):
            return 10
        if self.check_win_for(self.player):
            return -10
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "-":
                        self.board[row][col] = self.computer
                        score = self.minimax(False)
                        self.board[row][col] = "-"
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "-":
                        self.board[row][col] = self.player
                        score = self.minimax(True)
                        self.board[row][col] = "-"
                        best_score = min(best_score, score)
            return best_score
    
    def is_board_full(self):
        
        # Check if board is full.
        return all("-" not in row for row in self.board)

    def display_board(self):
        
        # Display current state of board.
        print("       Col1 Col2 Col3 ")
        print()
        print(f"Row 1  | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |")
        print("       +---+---+---+ ")
        print(f"Row 2  | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |")
        print("       +---+---+---+ ")
        print(f"Row 3  | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |")
        print()

    def check_win(self):
        
        # Check for winner.
        return (self.check_diagonal_win() or 
                self.check_horizontal_win() or 
                self.check_vertical_win())

    def check_win_for(self, symbol):
        
        # Check if a specific player has won.
        # Check diagonals
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol) or 
            (self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol)):
            return True
        
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == symbol:
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True
        
        return False

    def check_diagonal_win(self):
        
        # Check for win in diagonals.
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] != "-") or 
            (self.board[0][2] == self.board[1][1] == self.board[2][0] != "-")):
            return True
        return False

    def check_horizontal_win(self):
        
        # Check for win in rows.
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "-":
                return True
        return False

    def check_vertical_win(self):
        
        # Check for win in columns.
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "-":
                return True
        return False

    def switch_turn(self):
        
        # Switch turns between player and computer.
        self.whose_turn = 1 - self.whose_turn

if __name__ == "__main__":
    
    game = TicTacToe()
    game.start_game()