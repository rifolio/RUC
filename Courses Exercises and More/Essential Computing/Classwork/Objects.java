public class Objects {
    
    public static void main(String[] args) {

        String s = "This is";
        String t = s;

        s += " a test!";
        s= s.toUpperCase();

        System.out.println(s);
        System.out.println(t); 

        for (int i = 0; i < args.length ; i ++) {
            System.out.println (" Argument " + i + " is " + args[i]);
        }
    }
}
