# Python-TicTacToe
Updated a student Java project to learn Python- also made updates to the older code removing redundancies and adding the minimax algorithm to optimize computer's move choice.

ORIGINAL JAVA CODE:

import java.util.Random;
import java.util.Scanner;

public class TicTacToe {
    static Scanner scanner = new Scanner(System.in);
    static Random random = new Random();
    static char[][] board = {{'-', '-', '-'}, {'-', '-', '-'}, {'-', '-', '-'}};
    static boolean playerTurn = true; 
    static char playerMark;
    static char computerMark;
    
    public static void main(String[] args) {
        printIntroduction();
        
        // Get player's choice of marker
        playerMark = getPlayerMarker();
        computerMark = (playerMark == 'X') ? 'O' : 'X';
        
        System.out.println("You have selected '" + playerMark + "', so the computer will use '" + computerMark + "'!");
        
        boolean gameOver = false;
        while (!gameOver) {
            System.out.println();
            displayBoard();
            
            if (playerTurn) {
                playerMove();
                if (checkWin()) {
                    displayBoard();
                    System.out.println("Congratulations! You win!");
                    gameOver = true;
                }
            } else {
                computerMove();
                if (checkWin()) {
                    displayBoard();
                    System.out.println("Sorry! Computer wins! Please, try again!");
                    gameOver = true;
                }
            }
            
            // Check for draw only if no one has won
            if (!gameOver && isBoardFull()) {
                displayBoard();
                System.out.println("Draw!");
                gameOver = true;
            }
            
            playerTurn = !playerTurn;
        }
    }

    public static void printIntroduction() {
        System.out.println("Tic Tac Toe!\n");
        System.out.println("You will be able to select 'X' or 'O' as your marker.");
        System.out.println("Your goal is to match 3 of your markers in a row, horizontally, vertically, or diagonally.");
        System.out.println("To make your move, first select the Row #, and press ENTER.");
        System.out.println("Next, select the Column # and press ENTER to complete your move.");
        System.out.println("\nThe computer will then make its move.");
        System.out.println("The game board will be displayed after each move.");
        System.out.println("You will play the computer until either a winner is declared, or the game ends in a draw.");
        System.out.println("\nGOOD LUCK!");
        System.out.println();
    }
    
    public static char getPlayerMarker() {
        System.out.print("Would you like to play as 'X' or 'O'? ");
        String input = scanner.nextLine().toUpperCase();
        
        while (!(input.equals("X") || input.equals("O"))) {
            System.out.print("Invalid entry. Must choose 'X' or 'O': ");
            input = scanner.nextLine().toUpperCase();
        }
        
        return input.charAt(0);
    }

    public static void playerMove() {
        int row, col;
        boolean validMove = false;
        
        while (!validMove) {
            System.out.println("Your turn. Enter Row # (1-3): ");
            row = getValidNumber(1, 3) - 1;
            
            System.out.println("Enter Column # (1-3): ");
            col = getValidNumber(1, 3) - 1;
            
            if (board[row][col] == '-') {
                board[row][col] = playerMark;
                validMove = true;
            } else {
                System.out.println("Position occupied. Please try again.");
            }
        }
    }
    
    public static int getValidNumber(int min, int max) {
        int num = 0;
        boolean valid = false;
        
        while (!valid) {
            try {
                num = Integer.parseInt(scanner.nextLine());
                if (num >= min && num <= max) {
                    valid = true;
                } else {
                    System.out.println("Invalid entry. Please enter a number between " + min + " and " + max + ": ");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid entry. Please enter a number: ");
            }
        }
        
        return num;
    }
    
    public static void computerMove() {
        System.out.println("Computer's turn.");
        int row, col;
        
        do {
            row = random.nextInt(3);
            col = random.nextInt(3);
        } while (board[row][col] != '-');
        
        board[row][col] = computerMark;
    }

    public static boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '-') {
                    return false;
                }
            }
        }
        return true;
    }

    public static void displayBoard() {
        System.out.println("       Col1 Col2 Col3 ");
        System.out.println();
        System.out.println("Row 1  | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |");
        System.out.println("      ---------------");
        System.out.println("Row 2  | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |");
        System.out.println("      ---------------");
        System.out.println("Row 3  | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |");
        System.out.println();
    }
    
    public static boolean checkWin() {
        return (checkDiagWin() || checkHoriWin() || checkVertWin());
    }
    
    public static boolean checkDiagWin() {
        // Check main diagonal (top-left to bottom-right)
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != '-') {
            return true;
        }
        // Check other diagonal (top-right to bottom-left)
        return (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != '-');
    }
    
    public static boolean checkHoriWin() {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != '-') {
                return true;
            }
        }
        return false;
    }
    
    public static boolean checkVertWin() {
        for (int i = 0; i < 3; i++) {
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != '-') {
                return true;
            }
        }
        return false;
    }
}
