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
    print("======================================================")
    print("Hello There!",end=" ")
    print("Welcome to our Volume Calculator Program!")
    print("======================================================")
def Sphere(measurement):
    # Author:Jeff
    radius=measurement[0]
    V=(4/3)*math.pi*math.pow(radius,3)
    return V
    
def PentagonalPyramid(measurement):
    # Author:Harnoor
    baseedge=measurement[0]
    height=measurement[1]
    V=(5/12)*math.tan(0.942478)*height*math.pow(baseedge,2)
    return V

def RectangularPrism(measurement):
    # Author:Jeff
    length = measurement[0]
    height = measurement[1]
    width = measurement[2]
    V= length*height*width
    return V

def HexagonalPyramid(measurement):
    # Author:Harnoor
    baseedge=measurement[0]
    height=measurement[1]
    V=math.sqrt(3)/2*math.pow(baseedge,2)*height
    return V

def RectangularPyramid(measurement):
    # Author:Jeff
    BaseLength = measurement[0]
    BaseWidth = measurement[1]
    Height = measurement[2]
    V = (1/3)*BaseLength*BaseWidth*Height
    return V

def TriangularPrism(measurement):
    # Author:Jeff
    length = measurement[0]
    height = measurement[1]
    base = measurement[2]
    V= (1/2)*base*length*height
    return V

def TriangularPyramid(measurement):
    # Author:Jeff
    BaseLength = measurement[0]
    BaseHeight = measurement[1]
    Height = measurement[2]
    V = (1/3)*BaseLength*BaseHeight*Height*(1/2)
    return V

def Cone(measurements):
    # Author:Simon
    height = measurements[0]
    radius = measurements[1]
    volume = (height/3) * math.pi * math.pow(radius,2)
    return volume

def cylinder(measurement):
    # Author:Simon
    height = measurement[0]
    radian = measurement[1]
    volume = math.pi* radian * radian * height 
    return volume

def hexagonalprism(measurement):
    # Author:Simon
    a = measurement[0]
    height = measurement[1]
    volume = 3*math.sqrt(3)*math.pow(a,2)* height/2
    return volume 

def pentagonprism(measurement):
    # Author:Simon
    BaseEdge = measurement[0]
    height = measurement[1]
    volume = (1/4)*math.sqrt(5*(5+2*math.sqrt(5)))*math.pow(BaseEdge,2)*height
    return volume
def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:Harnoor
    # Modified:
    print("To start enter a number")
    print("1=Triangular Prism")
    print("2=Rectangular Prism")
    print("3=Pentagonal Prism")
    print("4=Hexagonal Prism")
    print("5=Triangular Pyramid")
    print("6=Rectangular Pyramid")
    print("7=Pentagonal Pyramid")
    print("8=Hexagonal Pyramid")
    print("9=Cone")
    print("10=Cylinder")
    print("11=Sphere")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    if shape==1:
        #TriPrism
        x=("Enter the Base Length")
        y=("Enter the Height")
        z=("Enter the Base Height")
        prompts=[x,y,z,1]
        return prompts    
    elif shape==2:
        #RecPrism
        x=("Enter the Length")
        y=("Enter the Height")
        z=("Enter the Width")
        prompts=[x,y,z,1]
        return prompts
    elif shape ==3:
        #PentPrism
        x=("enter the Base Edge")
        y=("enter the Height")
        prompts=[x,y,3]
        return prompts
    elif shape==4:
        #HexPyramid
        x=("enter the Base Edge")
        y=("enter the Height")
        prompts=[x,y,3]
        return prompts
    elif shape==5:
        #TriPyramid
        x=("Enter the Base Edge")
        y=("Enter the Base height")
        z=("Enter the Height")
        prompts=[x,y,z,1] 
        return prompts 
    elif shape==6:
        #RecPyramid
        x=("Enter the Base Length")
        y=("Enter the Base Width")
        z=("Enter the Height")
        prompts=[x,y,z,1] 
        return prompts
    elif shape==7:
        #PentPyramid
        x=("Enter the Base Edge")
        y=("Enter the Height")
        prompts=[x,y,3]
        return prompts
         
    elif shape ==8:
        #HexPyramid
        x=("Enter the Base Edge")
        y=("Enter the Height")
        prompts=[x,y,3]
        return prompts
    elif shape ==9:
        #Cone
        x=("enter the Height")
        y=("enter the Radius")
        prompts=[x,y,3]
        return prompts
    elif shape ==10:
        #Cylinder
        x=("enter the Height")
        y=("enter the Radius")
        prompts=[x,y,3]
        return prompts
        
    elif shape ==11:
        #Sphere
        x=("Enter the Radius")
        prompts=[x,2]
        return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # Author:Harnoor
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
    # Author:Harnoor
    title()
    run=(1)
    while run!=2 and run==1:
        instructions()
        a=int(input("Select which shape you wish to calculate"))
        b=getParams(a)
        c=getInputs(b)
        if a==1:
            answer=TriangularPrism(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again") 
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==2:
            answer=RectangularPrism(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again") 
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==3:
            answer=pentagonprism(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
    
        elif a==4:
            answer=hexagonalprism(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==5:
            answer=TriangularPyramid(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again") 
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==6:
            answer = RectangularPyramid(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1")) 
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        
        elif a==7:
            answer = PentagonalPyramid(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==8:
            answer =HexagonalPyramid(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==9:
            answer=Cone(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==10:
            answer=cylinder(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again") 
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        elif a==11:
            answer=Sphere(c)
            print(answer)
            run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
            while run>2 or run<=0:
                print("Invalid Command. Please try again")  
                run=int(input("If you wish to exit the program, enter 2. If not enter 1"))
        
    
        if run==(2):
            print("Thank you for using our Volume Calculator ")

         
    

main()
        
