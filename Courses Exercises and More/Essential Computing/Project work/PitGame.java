/* 
 * Code made by Vladyslav Horbatenko for Mini Project
 * Date: 22.11.2023
 * 1. The game is played on a board (grid) consisting of 20 × 20 cells. ✅
 * 2. Initially, all cells are free, and the player is located in cell (0, 0). ✅
 * 3. In each turn, the player can move in one of the four cardinal directions (north, east,
 * south, west). ✅
 * 4. In each turn, a random number (between 1 and 5) of pits is placed on random spaces
 * of the board that don’t already have a pit. ✅
 * 5. The game is won if the player reaches the goal cell (19, 19). ✅
 * 6. The game is over and the player loses, if they stand on a pit. ✅
 * 7. The game is also lost if the player get surrounded by pits or is not able to reach the
 * goal location anymore. ✅
 */

// --------------------Imports--------------------
import java.util.Random;
import java.util.Scanner;

// --------------------Game--------------------
public class PitGame {

    // constants
    private static final int BOARD_SIZE = 20;
    private static final char FREE_CELL = '.';
    private static final char PLAYER = 'X';
    private static final char PIT = 'o';
    private static final char GOAL = 'G';
    private static Random random = new Random();
    private static Scanner scanner = new Scanner(System.in);

    // game variables
    private char[][] board; // 2dm board array
    private boolean visited; // visited cells
    private int playerRow; // player row number
    private int playerCol; // player col number
    private int goalRow; // goal row number
    private int goalCol; // goal col number
    private boolean fellIntoPit = false; // checks if player fell into pit

    public PitGame() {
        board = new char[BOARD_SIZE][BOARD_SIZE]; // initiating board with 20x20 size
        // calling methods to fill all empty spaces with "o" and also to place player and goal on board
        initializeBoard();
        placePlayer();
        placeGoal();
    }

    //method to fill each cell with free_cell symbol using nested loop
    private void initializeBoard() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                board[i][j] = FREE_CELL;
            }
        }
    }

    //method to put player on board
    private void placePlayer() {
        playerRow = 0; //players coordinates can be changed
        playerCol = 0;
        board[playerRow][playerCol] = PLAYER; //assign player's position
    }

    //method to put a goal on board
    private void placeGoal() {
        goalRow = BOARD_SIZE - 1; //assign goal's position to the last cell in our board, no matter of its size
        goalCol = BOARD_SIZE - 1;
        board[goalRow][goalCol] = GOAL; //assigning goal position
    }


    //puts random amount of pits in random positions, that are not player or goal, for each round
    private void placePits() {
        int numPits = random.nextInt(5) + 1; //random number from 1 to 5
        for (int i = 0; i < numPits; i++) {
            int row;
            int col;
            do { //using do while loop from classes to assign random positions to pits ONLY IF they are not player\goal\pit
                row = random.nextInt(BOARD_SIZE);
                col = random.nextInt(BOARD_SIZE);
            } while (board[row][col] != FREE_CELL);

            board[row][col] = PIT; //new pit
        }
    }

    //method to display board game status (positions) in terminal
    //using nested loop to print each cell (we have used it in a class)
    private void printBoard() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                System.out.print(board[i][j] + "  ");
            }
            System.out.println();
        }
    }

    //checking if player is not trying to move outside of the board
    private boolean isValidMove(int newRow, int newCol) {
        return newRow >= 0 && newRow < BOARD_SIZE && newCol >= 0 && newCol < BOARD_SIZE;
    }

    //checking weather is the players position equal to the goal position = game is won
    private boolean isGameWon() {
        return playerRow == goalRow && playerCol == goalCol;
    }

    private boolean isGameLost() {
        // return board[playerRow][playerCol] == PIT;
        return fellIntoPit;
    }

    //method to assist new position to player
    private void makeMove(int newRow, int newCol) {
        if (board[newRow][newCol] == PIT) { // check if the new position contains a pit
            fellIntoPit = true;
        } else {
            board[playerRow][playerCol] = FREE_CELL;
            playerRow = newRow;
            playerCol = newCol;
            board[playerRow][playerCol] = PLAYER;
        }
    }
    

    // method that checks if goal is reachable starting from current player position
    private boolean isGoalReachable() {
        // creating a boolean 2D array that marks visited cells
        boolean[][] visited = new boolean[BOARD_SIZE][BOARD_SIZE];
        visited[playerRow][playerCol] = true; // makring current player position as visited

        // creating direction arrays that will help us to move up, down, left, and right
        int[] dr = {-1, 1, 0, 0}; //rows
        int[] dc = {0, 0, -1, 1}; //columns
        //used source: https://codepal.ai/code-generator/query/jLOJJA08/a-star-path-finder-algorithm 

        // implementing a queue
        java.util.Queue<int[]> queue = new java.util.LinkedList<>(); //creating a queue
        queue.offer(new int[]{playerRow, playerCol}); // enqueue the current player position used source: https://www.geeksforgeeks.org/queue-interface-java/

        // running BFS until the queue is empty
        while (!queue.isEmpty()) {
            // dequeue the current position
            int[] current = queue.poll();
            int row = current[0];
            int col = current[1];

            // checking all four directions
            for (int i = 0; i < 4; i++) {
                int newCol = col + dc[i];
                int newRow = row + dr[i];

                // checking if the new position is within the board size, have not been visited, and not a pit
                if (newCol >= 0 && newCol < BOARD_SIZE && newRow >= 0 && newRow < BOARD_SIZE && board[newRow][newCol] != PIT && !visited[newRow][newCol]) {
                    // if goal is reached
                    if (newRow == goalRow && newCol == goalCol) {
                        return true; // goal is reachable
                    }

                    // marking the new position as visited and enqueuing
                    visited[newRow][newCol] = true;
                    queue.offer(new int[]{newRow, newCol});
                }
            }
        }
        return false; // if goal is not reachable
    }
        
// --------------------Main loop--------------------

    //initiating the game, its variables, 'settings' and running main game loop
    public static void main(String[] args) {
        PitGame game = new PitGame();

        while (true) {
            game.placePits();
            game.printBoard();

            System.out.print("\nEnter your move (W/A/S/D)- ");
            String move = scanner.next().toUpperCase(); //making input non-case-sensitive
            
            int newCol = game.playerCol;
            int newRow = game.playerRow;

            switch (move) { //using switch statement to select one of the optional moves and relevant actions in cells based on user input
                case "W": 
                    newRow--; //go up
                    break;
                case "D":
                    newCol++; //go right
                    break;
                case "S":
                    newRow++; //go down
                    break;
                case "A":
                    newCol--; //go left
                    break;
                default: //if user inputs something other than W\A\S\D
                    System.out.println("Wrong key pressed. You can enter W, A, S, or D-");
                    continue; //continue the loop
            }

            if (game.isValidMove(newRow, newCol)) { //checking of the move user made is valid
                game.makeMove(newRow, newCol);

                if (!game.isGoalReachable()) { // Check if the goal is not reachable
                    game.printBoard();
                    System.out.println("Game over! The goal is unreachable. You lose!");
                    break;
                }

                if (game.isGameLost()) { //if user steps on a pit, he receives the message that we losses and game ends
                    game.printBoard();
                    System.out.println("Game over! You stepped on a pit. You lose!");
                    break;
                }

                if (game.isGameWon()) { //checking if user reacher the goal and congratulate the player with this
                    game.printBoard();
                    System.out.println("Congratulations! You reached the goal. You win!");
                    break; //clothing game afterwards
                }
            } else { //in case player tries to leave his "matrix"
                System.out.println("Invalid move. You cannot leave this board, its not Matrix.");
            }
        }
        scanner.close();
    }
}
