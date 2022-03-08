//Written by Liam Newell(newel183umn.edu)
// FractalDrawer class draws a fractal of a shape indicated by user input
import java.awt.Color;
import java.util.Scanner;

public class FractalDrawer { //FractalDrawer class that serves the purpose of taking shapes and creating a fractal pattern.
    private double totalArea=0;  // member variable for tracking the total area
    private String shape; // String variable that represents the shape that the user will give to create a pattern with.

    public FractalDrawer() {  // contructor method
      Scanner scan = new Scanner(System.in);
      System.out.println("Enter which shape you would like your fractal to be");
      shape = scan.nextLine();
      drawFractal(shape); // calls drawFractal method for shape variable
    }

    //TODO:
    // drawFractal creates a new Canvas object
    // and determines which shapes to draw a fractal by calling appropriate helper function
    // drawFractal returns the area of the fractal
    public double drawFractal(String type) { // Method that creates a Canvas object then determines which fractal pattern to draw and calls the corresponding method for that shapes fractal.
        Canvas drawing = new Canvas(800,800);
        if(type.equals("circle")){
          System.out.println("circle");
          drawCircleFractal(100.0,400.0,400.0,Color.RED,drawing,7); // calls drawCircleFractal at the middle position of the Canvas
          return totalArea;
        }
        if(type.equals("triangle")){
          System.out.println("triangle");
          drawTriangleFractal(200.0,200.0,300.0,450.0,Color.RED,drawing,7); // calls drawTriangleFractal at the middle position of the Canvas
          return totalArea;
        }
        if(type.equals("rectangle")){
          System.out.println("rectangle");
          drawRectangleFractal(200.0,200.0,300.0,300.0,Color.RED,drawing,7); //// calls drawRectangleFractal at the middle position of the Canvas
          return totalArea;
        }
        return totalArea;
    }


    //TODO:
    // drawTriangleFractal draws a triangle fractal using recursive techniques
    public double drawTriangleFractal(double width, double height, double x, double y, Color c, Canvas can, int level){
      if(level <= 0){ // This is the base case for the recursive techniques.
        System.out.println("Tri1");
        return totalArea;


      }
      if(level==7){ // This is the first level that the fractal pattern should start at.
        System.out.println("Tri2");
        Triangle tri = new Triangle(x, y, width, height);
        totalArea += tri.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        tri.setColor(c);
        can.drawShape(tri);
        // Recursively creates three new triangles at correct positions for pattern by calling drawTriangleFractal again at a lower level to eventually reach base case.
        drawTriangleFractal(width*0.5, height*0.5, x+(width/4), y+(height/2), c, can, level-1);
        drawTriangleFractal(width*0.5, height*0.5, x-(width/4), y-(height/2), c, can, level-1);
        drawTriangleFractal(width*0.5, height*0.5, x+(width*0.75), y-(height/2), c, can, level-1);
        return totalArea;
      }
      else{ // This else statement will contain all of the middle levels of the pattern.
        System.out.println("Tri3");
        Triangle tri = new Triangle(x, y, width, height);
        totalArea += tri.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        tri.setColor(c);
        can.drawShape(tri);
        // Recursively creates three new triangles at correct positions for pattern by calling drawTriangleFractal again at a lower level to eventually reach base case.
        drawTriangleFractal(width*0.5, height*0.5, x+(width/4), y+(height/2), c, can, level-1);
        drawTriangleFractal(width*0.5, height*0.5, x-(width/4), y-(height/2), c, can, level-1);
        drawTriangleFractal(width*0.5, height*0.5, x+(width*0.75), y-(height/2), c, can, level-1);
        return totalArea;
      }
    }


    // TODO:
    // drawCircleFractal draws a circle fractal using recursive techniques
    public double drawCircleFractal(double radius, double x, double y, Color c, Canvas can, int level) {
      if(level <= 0){ // This is the base case for the recursive techniques.
        System.out.println("Cir1");
        return totalArea;


      }
      if(level==7){ // This is the first level that the fractal pattern should start at.
        System.out.println("Cir2");
        Circle cir = new Circle(x, y, radius);
        totalArea += cir.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        cir.setColor(c);
        can.drawShape(cir);
        // Recursively creates four new Circles at correct positions for pattern by calling drawCircleFractal again at a lower level to eventually reach base case.
        drawCircleFractal(radius/2, x+radius, y+radius, c, can, level-1);
        drawCircleFractal(radius/2, x-radius, y+radius, c, can, level-1);
        drawCircleFractal(radius/2, x+radius, y-radius, c, can, level-1);
        drawCircleFractal(radius/2, x-radius, y-radius, c, can, level-1);
        return totalArea;
      }
      else{ // This else statement will contain all of the middle levels of the pattern.
        System.out.println("Cir3");
        Circle cir = new Circle(x, y, radius);
        totalArea += cir.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        cir.setColor(c);
        can.drawShape(cir);
        // Recursively creates three new triangles at correct positions for pattern by calling drawTriangleFractal again at a lower level to eventually reach base case.
        drawCircleFractal(radius/2, x+radius, y+radius, c, can, level-1);
        drawCircleFractal(radius/2, x-radius, y+radius, c, can, level-1);
        drawCircleFractal(radius/2, x+radius, y-radius, c, can, level-1);
        drawCircleFractal(radius/2, x-radius, y-radius, c, can, level-1);
        return totalArea;
      }
    }


    //TODO:
    // drawRectangleFractal draws a rectangle fractal using recursive techniques
    public double drawRectangleFractal(double width, double height, double x, double y, Color c, Canvas can, int level) {
      if(level <= 0){ // This is the base case for the recursive techniques.
        System.out.println("Rec1");
        return totalArea;


      }
      if(level==7){ // This is the first level that the fractal pattern should start at.
        System.out.println("Rec2");
        Rectangle rec = new Rectangle(x, y, width, height);
        totalArea += rec.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        rec.setColor(c);
        can.drawShape(rec);
        // Recursively creates four new Rectangles at correct positions for pattern by calling drawCircleFractal again at a lower level to eventually reach base case.
        drawRectangleFractal(width*0.5, height*0.5, x+width, y+height, c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x-(width/2), y+height, c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x+width, y-(height/2), c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x-(width/2), y-(height/2), c, can, level-1);
        return totalArea;
      }
      else{ // This else statement will contain all of the middle levels of the pattern.
        System.out.println("Rec3");
        Rectangle rec = new Rectangle(x, y, width, height);
        totalArea += rec.calculateArea();
        // following if else statements switch the colors based on levels.
        if(level%3==0){
          c = Color.RED;
        }
        else if(level%2==0){
          c = Color.BLUE;
        }
        else{
          c = Color.GREEN;
        }
        rec.setColor(c);
        can.drawShape(rec);
        // Recursively creates four new Rectangles at correct positions for pattern by calling drawCircleFractal again at a lower level to eventually reach base case.
        drawRectangleFractal(width*0.5, height*0.5, x+width, y+height, c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x-(width/2), y+height, c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x+width, y-(height/2), c, can, level-1);
        drawRectangleFractal(width*0.5, height*0.5, x-(width/2), y-(height/2), c, can, level-1);
        return totalArea;
      }
    }

    //TODO:
    // main should ask user for shape input, and then draw the corresponding fractal.
    // should print area of fractal
    public static void main(String[] args){ // Main Method creates FractalDrawer object which triggers whole program by calling the constructor
      FractalDrawer fract = new FractalDrawer();
      // double x=200.0;
      // double y=600.0;
      // double w=100.0;
      // double h=100.0;
      // Triangle tri = new Triangle(x, y, w, h);
      // Canvas drawing = new Canvas(800,800);
      // // Circle myCircle = new Circle(0,0,100);
      // // myCircle.setColor(Color.BLUE);
      // tri.setColor(Color.BLUE);
      // // drawing.drawShape(myCircle);
      // drawing.drawShape(tri);
      // tri = new Triangle(x+(w/4),y+(h/2),w*0.5,h*0.5);
      // drawing.drawShape(tri);
      // tri = new Triangle(x-(w/4),y-(h/2),w*0.5,h*0.5);
      // drawing.drawShape(tri);
      // tri = new Triangle(x+(w*0.75),y-(h/2),w*0.5,h*0.5);
      // drawing.drawShape(tri);

    }
}
