import java.util.*; 

public class input_homework {
    public static void main(String[] args) { //defining the main *
        Scanner sc= new Scanner(System.in); //making an input string stream
        System.out.print("What is you name- "); //receiving name of our user
        String name=sc.nextLine(); //saving the name
        System.out.println("Really nice to meet you, " + name); //printing output with received name
    }

}
