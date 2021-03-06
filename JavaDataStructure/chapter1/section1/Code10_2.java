package JavaDataStructure.chapter1.section1;

public class Code10_2 {
    public static void main(String[] args) {
        for(int n = 2; n <= 50; n++){
            boolean isPrime = true;
            // isPrime이 false면 반복문을 돌지 않도록 개선
            for(int i = 2; i*i <= n && isPrime; i++){ 
                if(n % i == 0) {
                    isPrime = false;
                }
            }
            if(isPrime){
                System.out.print(n+" ");
            }
        }
        System.out.println();
    }
}
