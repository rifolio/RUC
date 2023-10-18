/*
 NumberGuesser.java
 * User can play two different games by his choice,
 * In first game user will try to guess random number from 0 to 100
 * In second game user will help computer to guess him number from 0 to 100
 * Later you can evaluate who was better at guessing :)
 * 
 * Information used for second program: https://www.geeksforgeeks.org/binary-search/
 * 
 * Code made by Vladyslav Horbatenko for Assigment 3
 * Date: 10.11.2023
 */
import java.util.Random;
import java.util.Scanner;

public class NumberGuesser {
    //declaring variables that we can later use in both games
    private static int steps = 0;
    private static int rand_num = 0;
    private static int state = 1;
    private static Scanner scan = new Scanner(System.in);

    //creating the main function, where user can choose the game to play
    public static void main(String[] args) {
    
        System.out.print("We have two games: In first game you need to guess the number (type \'1\') In second - you help computer guess your number (type \'0\')- ");
        int choose = scan.nextInt(); //taking an input from user to decide which game we will play

        if (choose == 1) { 
                numberguess(); //running first game
        } else {    
            numberchooser(); //running second game
        }
    }


    //function that generates random numbers in our range
    public static int randomNum(int max) {
        Random rand = new Random();
        return rand.nextInt(max);
    }

    //logic and code for the first game
    public static void numberguess() {

        //generating random number for current game
        rand_num = randomNum(101);

        System.out.println("I have chosen a number between 1 and 100. Try to guess it!");

        //creating while loop to run process until we guess the right number, so state can be changed back to 0
        while (state == 1) {
            System.out.print("What is your guess- ");
            int guess = scan.nextInt();
            steps++;

            if (guess < rand_num) {
                System.out.println("The number is higher!");
            } else if (guess > rand_num) {
                System.out.println("The number is lower!");
            } else {
                System.out.println("Correct!");
                System.out.println("It took you " + steps + " attempts to guess this number!");
                state = 0; //exiting game by changing state to !1
            }
        }
    }

    //logic and code for the second game
    public static void numberchooser() {
        System.out.print("\nChoose a number between 0 and 100 in your head and indicate to the computer if the number you chose is higher (h), lower (l), or equal (e) to your number.\n");
    
        //setting up basic variables for our program
        //variable min and max as range in which unknown number is located
        int min = 0;
        int max = 100;
        int guess;
        String indicator = "false"; //indicator to run game until we guess the number
        
        //to solve this problem we will use binary search (we used to do something similar with Python)

        //creating while loop to play the game until computer guesses the number
        while (!indicator.equals("true")) {
            steps++; //counting steps
            guess = (min + max) / 2; //first guess just in between max and min
            System.out.print("Is your number " + guess + "?  (\'h\', \'l\', \'e\')--- ");
            indicator = scan.next();
    
            //taking user indicator
            if (indicator.equals("h")) {
                min = guess + 1; //changing minimum value
            } else if (indicator.equals("l")) {
                max = guess - 1; //changing maximum value
            } else if (indicator.equals("e")) {
                indicator = "true"; //stoping the while loop
                System.out.println("It took the computer " + steps + " attempt(s) to guess your number - " + guess);
            }
        }
    }
}