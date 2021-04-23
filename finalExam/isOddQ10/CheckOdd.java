public class CheckOdd {

    public static void main(String args[]) {
        System.out.println(isNumberOdd(3));   // should be 1
        System.out.println(isNumberOdd(10));  // should be 0
    }

    public static int isNumberOdd(int number) {
        if (number%2 == 0){
            return 0;
        }else{
            return 1;
        }
    }
}





