public class Fibonacci {

    public static void main(String args[]) {
        int N = 30;
        int nthFibo = computeNthFibo(N);  // jump to computeNthFibo, set value of that N to this N
        System.out.println(N);
    }

    public static int computeNthFibo(int N) { // this N has its own distinct memory slot!!!
        int previousValue = 1;
        int thisValue = 1;
        int nextValue;    // must *declare* variable OUTSIDE loop!!!
        while (N > 2) {
            nextValue = previousValue + thisValue;
            previousValue = thisValue;
            thisValue = nextValue;
           N = N - 1;
        }
        return thisValue;  // "return" jumps back to where this function was called
    }

}
