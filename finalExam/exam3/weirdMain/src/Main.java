public class Main {

    public static void main(String[] args) {
        int i = 0;
        increment(i);
        System.out.println(i); //This outputs 0 because i in main and i in increment are in different scopes
        //System.out.println(increment(i));
    }

    public static int increment(int i) {
        i++;
        return i; 
    }

}
