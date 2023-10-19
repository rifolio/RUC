/*
 * User can play two different games by his choice,
 * In first option you need to input password that program will "hack" 
 * In second - computer generates random password and "hacks" it 
 * 
 * In this case computer tries every possible number from 0 to 9 for each digit in array until its correct, after moving further
 * So in this case we assume that we can check weather the guessed digit was correct every time
 * Other version could be so that we try every possible combination for passwords (all at once) but that would take way more tries than method here
 * 
 * In case of email password "hacking" second method would be more realistic, as usually we can not check each symbol every time.  
 * 
 * Code made by Vladyslav Horbatenko for Assigment 4
 * Date: 19.11.2023
 */

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class BruteForceAttack {
    //basic variables and methods we'll need later
    private static Scanner scan = new Scanner(System.in);
    private static int sizepassword = 6;
    private static int password[] = new int[sizepassword];
    private static int guessed_password[] = new int[sizepassword];
    private static int tries = 0;

    public static void main(String[] args) {
        System.out.print("Choose an option (1 for user password, 0 for random password)- ");
        int choose = scan.nextInt(); //taking an input from user to decide which game we will play

        if (choose == 1) { 
            //taking user pawwsord input
            userPassword();
        } else {    
            //generating random password
            generateRandomPassword();
        }
        
        //calling main atack method
        bruteForce();

        //pinting guessed password
        System.out.println("The correct code is: " + Arrays.toString(password) +  "\n\nIt took " + tries + " to guess the password");
    }


    //option if we want to take users input as password
    public static void userPassword() {
        //taking user input (assuming its the password we aiming for further)
        System.out.print("Type in password numbers one by one. We'll try to to hack it!- ");
        for (int i=0; i<password.length; i++) {
            password[i] = scan.nextInt();
            if (i <(password.length - 1)) { //if condition so we won't receive "Next number-" when password is imputed already
                System.out.print("Next number- ");
            } 
        }
        System.out.println("\nUser password has been saved...");
    }
    

    //option if we want to generate a random password
    public static void generateRandomPassword() {
        Random rand = new Random();
        for (int i = 0; i < sizepassword; i++) {
            password[i] = rand.nextInt(10); //generating random number between 0 and 9
        }
        System.out.println("Random password has been generated...");
    }
    
    //method for attack, where we try every possible combination
    public static void generateRandomGuess() {
        //assigning 0 to all digits at first
        for (int i = 0; i < sizepassword; i++) {
            guessed_password[i] = 0;
        }

        //while function that goes through each digit of password comparing it to the same index in guessed_password, and tries numbers from 0 to 9 until its the same as in password. For each digit in array.
        int i = 0;
        while (!Arrays.equals(guessed_password, password)) {
            while (guessed_password[i] != password[i]) {
                guessed_password[i]++;
                tries++;
                System.out.println("Guess #" + tries + ": " + Arrays.toString(guessed_password));
                if (guessed_password[i] > 9) {
                    guessed_password[i] = 0; //resetting i to 0 for a new round (new index in array)
                }
            }
            i++; //moving to the next digit
        }
    }
    
    //Brute Force Attack method itself. printing out when its started and when successfully ended
    public static void bruteForce() {
        System.out.println("Brute-force attack started...");
        
        generateRandomGuess();

        System.out.println("Brute-force attack successful!");
    } 
}