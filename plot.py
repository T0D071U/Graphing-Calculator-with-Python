# --- Imports ---
import turtle as trtl

# --- setup ---

# --- functions ---
def newGraph(list):
  global cords, line, wn
  wn = trtl.Screen()
  wn.tracer(False)
  wn.title("Graph")
  line = trtl.Turtle()
  line.hideturtle()
  cords = trtl.Turtle()
  cords.hideturtle()
  cords.shape("circle")
  cords.color("red")
  cords.resizemode("user")
  cords.shapesize(.1, .1, .1)
  graphArea(list)
  wn.tracer(True)
  wn.onscreenclick(buttonclick,1)
  wn.listen()
  wn.mainloop()
  global first



def graphArea(list):
  yAxis = trtl.Turtle()
  yAxis.hideturtle()
  yAxis.setpos(0, -200)
  yAxis.goto(0, 200)
  
  xAxis = trtl.Turtle()
  xAxis.hideturtle()
  xAxis.setpos(-200, 0)
  xAxis.goto(200, 0)
  genericGraph(list)
  

def genericGraph(list):
  line.penup()
  cords = list[0]
  previous = cords
  line.goto(cords[0], cords[1])
  line.pendown()
  for i in list:
    top = i[1] - previous[1]
    bottom = i[0] - previous[0]
    slope = top / bottom
    if slope < 0:
      line.color("green")
    else:
      line.color("purple")
    line.goto(i[0]*10, i[1]*10)
    previous = i

def buttonclick(x,y):
  cords.clear()
  cords.penup()
  wn.tracer(False)
  cords.goto(x, y)
  wn.tracer(True)
  cords.pendown()
  cords.stamp()
  cords.pu()
  cords.forward(5)
  cords.pd()
  cords.write("[{0},{1}]".format((x/10), (y/10)))


