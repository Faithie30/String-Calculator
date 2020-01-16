public class Calculator {

    static int add(int x, int y){
        return x + y;
    }
    static int add(int...a){
        int sum = 0;
        for (int c = 0; c<a.length; c++){
            sum = sum + a[c];
        }
        return sum;
    }
    static int multiply(int x, int y){
        return x * y;
    }
    static int multiply(int... a){
        int result = 1;
        for (int c = 0; c<a.length; c++){
            result = result* a[c];
        }
        return result;
    }

}
