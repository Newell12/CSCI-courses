import java.util.Scanner;

public class Histogram {

  private int lowerbound;
  private int upperbound;
  private int[] lst;

  public Histogram(int lower, int upper){
    this.lowerbound = lower;
    this.upperbound = upper;
    lst = new int[upperbound - lowerbound + 1];
  }

  public boolean add(int i){
    if (i >= lowerbound && i <= upperbound){
      lst[(i-lowerbound)] = lst[(i-lowerbound)] + 1;
      System.out.print(i);
      return true;
    }
    else {
      return false;
    }
  }

  public String toString(){
    String output = "";
    String asterisks = "";
    for(int i = 0; i<lst.length; i++){
      System.out.println(lst[i]);
    }
    for (int i=lowerbound;i<=upperbound;i++){
      for (int g = 0; g < lst[i-lowerbound]; g++){
        asterisks += "*";
      }
      output += i + ":" + asterisks + "\n";
      asterisks = "";
    }
    return output;
  }

  public static void main(String[] args){
    // Histogram a = new Histogram(0, 5);
    // a.add(3);
    // a.add(2);
    // a.add(1);
    // a.add(2);
    // a.add(3);
    // a.add(4);
    // a.add(5);
    // System.out.println(a.toString());
    HistogramApp HistA = new HistogramApp();
  }
}
