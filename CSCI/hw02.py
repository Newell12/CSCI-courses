import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians

# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Converts from Celsius to Fahrenheit
    Parameter(s):
        celsius: The temperature of an environment in Celsius
    Return Value:
        The given temperature's measure in Fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        Prints five seperate lines of five stars totaling 25 stars
    Parameter(s):
        None
    Return Value:
        None
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')

# Part B: Write out a few simple conversions
def circumference_circle(radius):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        Calculates the circumference of a circle
    Paramter(s):
        radius: the distance from the center of a circle to its outer edge
    Return Value:
        The circumference of said circle based upon given radius
    '''
    return 2.0*math.pi*radius

def miles_to_kilometers(miles):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        Converts from miles to kilometers
    Parameters(s):
        miles: provided distance in miles
    Return Value:
        The given distance's measure in kilometers
    '''
    return miles*1.609344

def minutes_to_days(minutes):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        Converts from minutes into days
    Parameter(s):
        minutes: provided amount of time in minutes
    Return Value:
        The given amount of time in days
    '''
    return minutes/1440

# Part C: Calculate flight time based on initial speed, height, and angle
def trajectory(speed, height, angle):
    #print("TODO: Document and write this function")
    '''
    Purpose:
        Calculate how far a ball will fly before hitting the ground within a vaccume chamber
    Parameter(s):
        speed: the initial speed at which the ball was thrown in meters/second
        height: the height in meters from which the ball was thrown relative to the ground
        angle: the angle in degrees relative to the ground at which the ball was thrown
    Return Value:
        The amount of distance the ball will travel before hitting the ground
    '''
    horizontal_speed = speed*math.cos(degrees_to_radians(angle))
    vertical_speed = speed*math.sin(degrees_to_radians(angle))
    flight_time = (vertical_speed + math.sqrt((vertical_speed**2) + (19.6*height)))/9.8
    print('Horizontal Speed:', horizontal_speed,'m/s' )
    print('Vertical Speed:',vertical_speed,'m/s')
    print('Flight Time:',flight_time,'s')
    return flight_time*horizontal_speed
