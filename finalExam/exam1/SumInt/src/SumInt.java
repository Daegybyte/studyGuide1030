public class SumInt {

    public static void main(String args[]) {
        int LIMIT = 10;
        int answer = sumInts(LIMIT);   // sumInts has the value stored in LIMIT as maxInt
        System.out.println(answer);
    }

    public static int sumInts(int maxInt) {
        int i = 1;                // declare an integer "i" and set it to 1
        int sum;                  // declare an integer "sum"
        sum = 0;                  // we can combine this line with the previous one
        while (i <= maxInt) {     // remember, it's opposite day in Scratch loops!
            sum = sum + i;
            i = i + 1;
        }
        return sum;               // above, sumInts(LIMIT) is whatever this returns
    }

}