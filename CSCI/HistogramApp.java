import java.util.Scanner;
public class HistogramApp {

  private int lowerbound;
  private int upperbound;
  Histogram hist;

  public HistogramApp(){
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter the lowerbound:");
      lowerbound = scan.nextInt();
      System.out.println("Enter the upperbound:");
      upperbound = scan.nextInt();
      hist = new Histogram(lowerbound, upperbound);
      int str = 0;
      int str1 = 0;
      int str2 = 0;

      while(str<50){
        System.out.println("Enter a number greater than 50 if you would like to add a number or less than 50 to skip");
        str1 = scan.nextInt();
        if(str1>50){
          System.out.println("Enter a number to the Histogram: ");
          hist.add(scan.nextInt());
        }
        System.out.println("Enter a number greater than 50 if you would like to print the Histogram or less than 50 to skip");
        str2 = scan.nextInt();
        if(str2>50){
          System.out.println(hist.toString());
        }
        System.out.println("Enter a number greater than 50 to quit or less than 50 to continue");
        str = scan.nextInt();
      }
  }
}
