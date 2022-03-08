//Written by Liam Newell(newel183umn.edu)
import static java.lang.Math.PI;
import java.awt.*;
public class Circle{ //Circle Class that represents a Circle shape
  private double xpos; //x-position of Circle in center
  private double ypos; //y-position of Circle in center
  private double radius; //radius of Circle
  private Color color; //color of Circle

  public Circle(double x, double y, double rad){ //Constructor for Circle class
    xpos = x;
    ypos = y;
    radius = rad;
  }

  public double calculatePerimeter(){ //Method that Calculates the Perimeter of the Circle
    return (PI*2*radius);
  }

  public double calculateArea(){ //Method that calculates the Area of the Cirlce
    return (PI*Math.pow(radius,2));
  }

  public void setColor(Color c1){ //Method that sets the color of the Circle to a new color
    color = c1;
  }

  public void setPos(double x1, double y1){ //Method that sets the position of the Circle by giving a new xposition and yposition
    xpos = x1;
    ypos = y1;
  }

  public void setRadius(double rad1){ //Method that sets the height of the Cirlce to a new height
    radius = rad1;
  }

  public Color getColor(){ //Method that sets the color of the Circle to a new color
    return color;
  }

  public double getXPos(){ //Method that returns the current xposition of the Circle
    return xpos;
  }

  public double getYPos(){ //Method that returns the current yposition of the Circle
    return ypos;
  }

  public double getRadius(){ //Method that returns the current radius of the Circle
    return radius;
  }
}
