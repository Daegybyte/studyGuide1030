public class Counter {

    public static void main(String args[]) {
        System.out.println(count(1));
    }

    public static int count(int n) {    
        while (n > 0) {
            n = n + 1;
        }
        return n;
    }

}