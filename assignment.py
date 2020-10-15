#python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:Harnoor
    # Modified:
    print("Welcome to our program")

def Sphere(measurement):
    radius=measurement[0]
    V=(4/3)*math.pi*math.pow(radius,3)
    return V
    
def PentagonalPyramid(measurement):
    baseedge=measurement[0]
    height=measurement[1]
    V=(5/12)*math.tan(0.942478)*height*math.pow(baseedge,2)
    return V

def RectangularPrism(measurement):
    length = measurement[0]
    height = measurement[1]
    width = measurement[2]
    V= length*height*width
    return V

def HexagonalPyramid(measurement):
    baseedge=measurement[0]
    height=measurement[1]
    V=math.sqrt(3)/2*math.pow(baseedge,2)*height
    return V

def RectangularPyramid(measurement):
    BaseLength = measurement[0]
    BaseWidth = measurement[1]
    Height = measurement[2]
    V = (1/3)*BaseLength*BaseWidth*Height
    return V

def TriangularPrism(measurement):
    length = measurement[0]
    height = measurement[1]
    base = measurement[2]
    V= (1/2)*base*length*height
    return V

def TriangularPyramid(measurement):
    BaseLength = measurement[0]
    BaseHeight = measurement[1]
    Height = measurement[2]
    V = (1/3)*BaseLength*BaseHeight*Height
def Cone(measurements)
    height = measurements[0]
    radius = measurements[1]
    p = math.pi
    volume = (height/3) * math.pi * radius * radius * height
    return volume

def cylinder(measurement)
    height = measurements[0]
    radian = measurements[1]
    volume = math.pi* radian * radian * height 
    return volume

def hexagonalprism(measurement)
    BaseEdge = a
    a = measurement[0]
    height = measurement[1]
    volume = 3 * math.sqrt(3) * a * a * h/2
    return volume 

def pentagonprism(measurement)
    BaseEdge = measurement[0]
    height = measurement[1]
    volume = (5 * BaseEdge * height) /2
    return volume
def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("1=Rectangular Prism")
    print("2=Triangular Prism")
    print("3=Sphere")
    print("4=cylinder")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    if shape==1:
        x=("Enter the length")
        y=("Enter the height")
        z=("Enter the width")
        prompts=[x,y,z,1]
        return prompts
    elif shape==2:
        x=("Enter the length")
        y=("Enter the height")
        z=("Enter the base")
        prompts=[x,y,z,1]
        return prompts
    elif shape ==3:
        x=("Enter the Radius")
        prompts=[x,2]
        return prompts
    elif shape==4 or 5:
        x=("Enter the Base edge")
        y=("Enter the height")
        prompts=[x,y,3]
        return prompts
    elif shape==6 or 7:
        x=("Enter the Base edge")
        y=("Enter the Base height")
        z=("Enter the height")
        prompts=[x,y,z,1] 
        return prompts 
    elif shape ==8:
        x=("enter the length")
        y=("enter the radius")
        prompts=[x,y,3] 
        return prompts
     elif shape ==9:
        x=("enter the length")
        y=("enter the radian")
        prompts=[x,y,3]
        return prompts
     elif shape ==10:
        x=("enter the base edge")
        y=("enter the height")
        prompts=[x,y,3]
        return prompts
     elif shape ==11:
        x=("enter the base edge")
        y=("enter the height")
        prompts=[x,y,3]
        return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements=[]
    
    if questions[-1]==1:
        a=int(input(questions[0]))
        a=measurements.insert(0,a)
        b=int(input(questions[1]))
        b=measurements.insert(1,b)
        c=int(input(questions[2]))
        c=measurements.insert(2,c)
        print(measurements)
        return measurements
    
    elif questions[-1]==2:
        a=int(input(questions[0]))
        a=measurements.insert(0,a)
        return measurements
    elif questions[-1]==3:
        a=int(input(questions[0]))
        a=measurements.insert(0,a)
        b=int(input(questions[1]))
        b=measurements.insert(1,b)
        return measurements
    
def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    run=(1)
    while run!=2:
        instructions()
        a=int(input("Select which shape you wish to calculate"))
        b=getParams(a)
        c=getInputs(b)
        if a==1:
            answer=RectangularPrism(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==2:
            answer=TriangularPrism(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==3:
            answer=Sphere(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
    
        elif a==4:
            answer=PentagonalPyramid(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==5:
            answer=HexagonalPyramid(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==6:
            answer = RectangularPyramid(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1")) 
        elif a==7:
            answer = TriangularPyramid(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==8:
            answer =Cone(c)
            print(answer)
            run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==9:
                answer=cylinder(c)
                print(answer)
                run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==10:
                answer=hexagonalprism(c)
                print(answer)
                run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
        elif a==11:
                answer=pentagonprism(c)
                print(answer)
                run=int(input("If u wish to exit the program, enter 2. If not enter 1"))
main()
main()
