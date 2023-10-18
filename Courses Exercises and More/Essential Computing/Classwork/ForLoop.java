import java.util.*;

public class ForLoop {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input the first number- "); //receiving 1st number from user
        int a = input.nextInt(); //saving the 1st numbers
        System.out.print("Input the second number- "); //receiving 2nd number from user
        int b = input.nextInt(); //saving the 2nd number

//        int a = 10; int b= 10;

        for (int i = 1; i <= a; i ++) {
            for (int j = 1; j <= b; j ++) {
                System.out.printf ("%1.5E ", Math.pow(i, j));
            }
            System.out.println () ;
        }
    }


// String s = "This is a test!"
// s.substring(10) - starting from 10
// s.substring(4,10) - from 4th to 10th

// How to find index of something?
// String fruit = "banana"
// fruit.indexOf('a') - returns 1 (index of first appearance of 'a')

//How to compare strings?
// s.equals(t)
    //- returns TRUE if the character sequences in s and t are identical
    // - returns FALSE if the sequences in s and t are different
// s.compareTo(t)
    // -returns 0 if characters sequences in s and t are identical
    // -returns a positive value if the character sequence in s comes lexicographically after that in t
    // -returns a negative value if the character sequence in s comes lexicographically before that in t

// Also important to use s.toUpperCase() methods or lowercase as this things are case-sensitive


//The String class implements a number of methods, such as:
    //charAt(int n) - returns the character with index n.
    //compareTo(String s) - returns a comparison of two strings.
    //concat(String s) - same as += s.
    //equals(String s) - returns true if two strings have the same contents.
    //indexOf(char c) - returns the first position of the character c in the string.
    //indexOf(String s) - returns the first position of the substring s in the string.
    //isEmpty() - returns true if the string is empty (== "")
    //lastIndexOf(String s) - returns the last position of the substring s in the string
    //length() - returns the number of characters in the string.
    //replace(String s, String t) - returns a string where instances of substring s are replaced with substring t.
    //split(String c) - returns a String array containing substrings delimited by the characters in c.
    //substring(int n) - returns the substring beginning with index n.
    //substring(int n, int m) - returns the substring beginning with index n and ending with index m-1.
    //toCharArray() - returns a char array with the string characters.
    //toLowerCase() - returns a String where all characters are converted to lower case.
    //toUpperCase() - returns a String where all characters are converted to upper case.
    //trim() - returns a string where leading and trailing whitespace has been removed.

//    public static boolean testLetterHist(String s, int[] expectedresult) {
//        int[] result = letterHist(s);
//        System.out.println();
//
//        System.out.printLn(Arrays.toString(result));
//
//        System.out.println("Should give: ");
//        System.out.println("{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}");
//
//        return indentical;
    }

// }