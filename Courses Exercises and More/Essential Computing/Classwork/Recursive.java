
public class Recursive {
    public static void main(String[] args) { //creating the main to run other methods
        System.out.println(addSum(20));
    }
    
        
    public static int addSum(int n) { //our method
        int result;
        if (n <= 0 || n % 2 == 0) { //checking weather the imputed number is negative or even if so do else
            System.out.println("You can only input odd positive numbers");
            return -1;
        } else { //the main function which is only executed in case of odd positive imputed number
            if (n == 1) {
                result = 1;
            } else {
                result = n + addSum(n - 2);
            }
            return result;              
        }
    }
}