
print('Lets Create Patterns!')
#Taking Valid input from user
ColourList = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white'] #List of Colour options
print(ColourList) #printing the list
bgc = ' '#variable to store bgcolour input
while bgc not in ColourList: #checking if colour variable matches colour option in Bgcolour list
    bgc = input('Choose a Bg Colour: ')#taking colour input

Penclr = ' '#variable to store the input
while Penclr not in ColourList: #checking if colour variable matches colour option in the option list
    Penclr = input('Choose Stroke Colour: ')#taking input

Shapeclr = ' '#variable to store the input
while Shapeclr not in ColourList: #checking if colour variable matches colour option in the option list
    Shapeclr = input('Choose Shape Colour: ')#taking input

Shapes = {'0': 'square', }
for num, shape in Shapes.items():
   print(num, shape)
Shapes = ['square', 'star', 'triangle', 'circleX', 'flower' , 'starcircle', 'turtle star'] #List of options
print(Shapes) #printing the list
Shape = ' '#variable to store the input
while Shape not in Shapes: #checking if shape input given matches shape option in the Shapes list
    Shape = input('Choose a Shape: ')#taking input

Size = 0 #sidelength multiplier variable
while Size < 1 or Size > 10: #input posibility only for numbers b/w 1-10
    Size = float(input('Enter Shape Size(1-10): ')) #taking input as float to get input as numeric 

Distance = 0 #Gap Distance multiplier variable
while Distance < 1 or Distance > 10: #input posibility only for numbers b/w 1-10
    Distance = float(input('Enter Distance b/w Shapes(1-10): ')) #taking input as float to get input as numeric 

#______________________________________________________________
# bgc = "white"
# Penclr = "black"
# Shapeclr = "red"
# Shape = "star"
# Size = 5
# Distance = 10

from math import floor #importing floor math for making calculated value to adjacent lower integer
import turtle
t = turtle.Turtle() #Brought t variable acting as turtle
turtle.tracer(0, 0) #made tracer 0,0 for not tracing the drawing so as to get instant pattern output
turtle.bgcolor(bgc) #assinging input Background clour
a = t.getscreen() 
a.setup(width=900, height =620) #seted a fixed size for the opening up turtle graphics screen


#______________________________________________________________

def draw_shape(Shape, Penclr, Shapeclr, Size):#defining a function 'draw_shape' for drawing different shapes by using the variables
    t.pendown() 
    t.speed(0)
    xy = t.pos()#saving the initial position of the turtle
    t.color(Penclr , Shapeclr)
    t.begin_fill()

    if Shape == 'star': # Shapes[shp_num] == 'star'
        for i in range(5):#drawing a star
            t.forward(Size*4)
            t.right(144)

    if Shape == 'square':
        for i in range(4):
            t.forward(Size*4)
            t.right(90)

    if Shape == 'triangle':
        for i in range(3):
            t.forward(Size*4)
            t.left(120)

    if Shape == 'flower':
        for i in range(50): 
            t.forward(Size*8)
            t.right(155)            

    if Shape == 'starcircle':
        for i in range(77):
            t.forward(Size*6)
            t.right(146)

    if Shape == 'circleX':
        for i in range(180):
            t.forward(Size*5)
            t.right(30)
            t.forward(Size)
            t.left(60)
            t.forward(Size*2.5)
            t.right(30)

            t.penup()
            t.setposition(xy)
            t.pendown()

            t.right(2)

    if Shape == 'turtle star':
        for i in range(36):
            t.forward(100)
            t.left(170)
    
    t.end_fill()
    t.penup()
    t.setposition(xy)#moving the turtle back to the initial saved position
    t.setheading(0) #making the turtle point right/east so as to always move forward in right direction after each shape

#______________________________________________________________

shape_distance = Distance*20 #the distance between two  shapes
width = floor((900/(Size + shape_distance)) + 1)#calculating the no.of shapes that could draw in a row,so that the width of the scren is completely utilised and saving the data in the variable width
height = floor((600/(Size + shape_distance)) + 1)#calculating the no.of shapes that could draw in a coloum,so that the height of the scren is completely utilised and saving the data in the variable height

t.speed(0)
t.penup()
t.goto(-440,280) #starting position set to left corner of the opening up turtle graphics screen

for y in range(height): #repeatation of rows drawing 
    for i in range(width): #repetation of shape drawing 
        draw_shape(Shape = Shape, Penclr = Penclr, Shapeclr = Shapeclr, Size = Size)#calling the function for drawing shapes
        t.forward(shape_distance) #giving gap between shapes
    t.backward(shape_distance * width)#returning to the left of the screen
    t.right(90)#going to next row
    t.forward(shape_distance)
    t.left(90)

turtle.done() 

#______________________________________________________________

#Further Plans - 
## Increase the Shape Options
## Replace of Option Lists to Dictianery, So as to make it easier for the User to give input
# Print invalid input, while asking again for input
##### User statisfaction enqury and retake input variables that the user want to change
### Colour Code input validatation
#### Different kind of pattern formation (Similar to certain kind of real pattern)

