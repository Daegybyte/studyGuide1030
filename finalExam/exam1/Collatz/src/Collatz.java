public class Collatz {

    public static void main(String args[]) {
        int STARTING_N = 50000;
        int answer = computeCollatzSequence(STARTING_N);
        System.out.println(answer);
    }

    public static int computeCollatzSequence(int N) {
        N = N;
        while(N != 1){
            if(N %2 == 0){
                N = N/2;
            }else{
                N = (3*N)+1;
            }

        }return N;
    }

}