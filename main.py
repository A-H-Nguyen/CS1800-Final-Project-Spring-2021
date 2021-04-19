import turtle
import numpy
import random

uin = input("Input the cardinality of a set as an integer:")
n = int(uin) #polygon of side n
permut = numpy.math.factorial(n) #we will need this for later
ang_sliced = 360 / n #we're going to be cutting up the polygons like a pizza. 360 / 5 would give 72 degrees, which allows us to construct a pentagon

s = turtle.getscreen() #initializing turtle screen
t = turtle.Turtle() #initializing turtle

t.shape("turtle") #I could've just kept it as a triangle, but this is much cuter

t.begin_poly() #after drawing the wedge lines I will be able to get the points the turtle draws up to, these will be the polygon's vertices
t.fd(200)#drawing the first line, which is a vertical line
i = 1
while i < n: #this while loop is drawing lines that the sliced polygon will be drawn around
    t.home()
    t.rt(ang_sliced * i)
    t.fd(200)
    i += 1
t.end_poly()
points = t.get_poly() #we will use the points in p to draw the actual edges of the polygon

#the first term in p is always (0.00,0.00), and we don't want that:
points = list(points) #Turns out p is a tuple not a list, so I can't just use pop
points.pop(0)

#here I have a little algorithm to actually draw and fill in the wedges:
j = 0 #we want to draw wedges for each of the permutations of a set with cardinality n 
while j < permut: 
    t.clear() #every iteration I am clearing the screen and initializing a new turtle
    t = turtle.Turtle() #This helps a lot with performance with big sets (by big, I mean any set of n >= 5)
    t.shape("turtle")
    t.speed(8) #we want a pretty fast turtle, but if it's too fast we won't really be able to see most of the permutations

    print("Permutation number", (j+1), "of", permut) #keep track of how many permutations have been displayed

    i = 0 
    while i < (len(points)+1):
        #I want a color code for each wedge drawn. So here's a quick algorithm I got from: https://www.codespeedy.com/create-random-hex-color-code-in-python/
        random_num = random.randint(0,16777215) 
        hex_num = str(hex(random_num))
        hex_num ='#'+ hex_num[2:] #all this does is generate a random hex number
        while len(hex_num) != 7: #however, this algorithm doesn't always give a 6 digit hex number
            random_num = random.randint(0,16777215)
            hex_num = str(hex(random_num))
            hex_num ='#'+ hex_num[2:]
            #this will keep generating a new hex number as long as it is not the correct amount of digits

        #theoretically, there are enough random colors generated such that every permutation gets its own set of colored wedges
        #This is actually a false notion, however there are only 16777215, and even 11! is already waaaaay bigger than this
        #by simply ignoring the fact that there will be duplicate colors, we will be able to look at more permutations!
        t.fillcolor(hex_num) 

        #Now we can actually draw these wedges:
        if i < len(points) - 1: #this if statement draws n-1 wedges
            wedge = [points[i], points[i+2]]
            t.begin_fill()
            t.home()
            t.goto(wedge[0])
            t.goto(wedge[1])
            t.home()
            t.end_fill()
        elif i >= len(points) - 1: #This little elif statement is for drawing the nth wedge:
            t.begin_fill()
            t.home()
            t.goto(points[-1])
            t.goto(points[0])
            t.home()
            t.end_fill() 
        i += 2
    j += 1

turtle.Screen().exitonclick()
