class Hello 
{
  public static void main(String[] args) {

    int n = 5, i, x; 

    for (i = 1 ; i <= n; i ++) {

        for (x = 1; x <= n; x ++) {
            System.out.print(x * i + "");
        }
        
        System.out.println();

    }
  }
}
