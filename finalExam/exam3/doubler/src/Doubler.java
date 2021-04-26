//this program outputs 2^x

public class Doubler {

    public static void main(String args[]) {
        int x = 4;
        System.out.println(doubler(x));
    }

    public static int doubler(int n) {
        int result = 1;
        while (n > 0) {
            result = result + result;
            n = n - 1;
        }
        return result;
    }

}