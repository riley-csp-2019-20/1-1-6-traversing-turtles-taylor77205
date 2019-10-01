#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  turtle = trtl.Turtle(shape=s)
  my_turtles.append(turtle)

#  sarting position 
startx = 0
starty = 0

#make turtle move
for turtle in my_turtles:
    turtle.up()
	turtle.goto(startx, starty)
    turtle.down()
	turtle.right(45)     
	turtle.forward(50)
    count+=1
#	amount turtle will move 
	startx = startx 
	starty = starty 

wn = trtl.Screen()
wn.mainloop()