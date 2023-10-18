//Vladyslav Horbatenko, Assigment 2

import java.util.Scanner; //must have imports

public class NumberAnalyzer { //setting up the program
    public static void main(String[] args) { //main class
        Scanner scan = new Scanner(System.in);

        while (true) {
            System.out.print("Enter your number- "); //asking user to input number (that will be analyzed later)
            int number = scan.nextInt();

            // checking if number even or odd using if conditions
            if (number % 2 == 0) { //if number can be devided by 2 - even
                System.out.println(number + " is an even number");
            } else { //otherwise its odd
                System.out.println(number + " is an odd number");
            }

            // checking if the number is positive, negative or zero using if conditions
            if (number < 0) { //less than zero - negative
                System.out.println("Your number is negative... ");
            } else if (number > 0) { //more than zero - negative
                System.out.println("Your number is positive... ");
            } else { //otherwise its just zero
                System.out.println("Your number is... zero, not the best choice of a number, try something else");
            }
        }
    }
}
