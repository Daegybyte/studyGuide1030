public class Multiply {

    public static void main(String args[]) {
        System.out.println(mysteryFunction(2,3));
    }

    public static int mysteryFunction(int x, int y) {
        int result = 0;
        while (x > 0) {
            result = result + y;
            x = x - 1;
        }
        return result;
    }

}