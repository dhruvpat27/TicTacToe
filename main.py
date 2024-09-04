import turtle as trtl
t = trtl.Turtle()
#make grid
t.speed(100)
t.penup()
x = -105
y = 105
t.goto(x,y)
t.pendown()
t.hideturtle()
dis = 210
intr = 70
#delete below for loop (outer box) when done with buttons
for a in range (4):
  t.forward(dis)
  t.right(90)
for b in range(2):
  t.penup()
  y = y - (dis / 3)
  t.goto(x, y)
  t.pendown()
  t.forward(dis)
y = 105
t.right(90)
for c in range(2):
  t.penup()
  x = x + (dis / 3)
  t.goto(x,y)
  t.pendown()
  t.forward(dis)



def drawX(xCor, yCor):
  t.setheading(0)
  xCor += 10
  yCor -= 10
  t.penup()
  t.color("red")
  t.pensize(5)
  t.goto(xCor, yCor)
  t.pendown()
  t.right(45)
  t.forward(70.7106781)
  t.penup()
  t.goto(xCor + 50, yCor)
  t.right(90)
  t.pendown()
  t.forward(70.7106781)

def drawO(xCor, yCor):
  t.setheading(0)
  t.penup()
  t.goto(xCor + 35, yCor - 65)
  t.pendown()
  t.pensize(5)
  t.color("blue")
  t.circle(30)
#def checkBox(num, list):
# print("ye")
def storeList(listNew, listOld):
  for x in listOld:
    listNew.append(x)
moveListGlo = []
def addToMoveList(boxNumber, list, play1, play2):
  list.append(boxNumber)
  if(len(play1) % 2 == 0): play1.append(boxNumber)
  else: play2.append(boxNumber)
def buttonClick(xPar, yPar):
  x = -105 
  y = 105
  # try making it so that this code is object oriented, associate coordinates with a square.  
  moveList = []
  play1Moves = []
  play2Moves = []
  num = 0
  t.speed(5)
  if (-105 < xPar < -35): 
    x = -105
    if (105 < yPar < 35): 
      num = 1
      y = 105
    elif (-35 < yPar < 35): 
      num = 2
      y = 35
    elif (-105 < yPar < -35): 
      num = 3
      y = -35
    addToMoveList(num, moveList, play1Moves, play2Moves)
  if ((-35) < xPar < (35)): 
    x = -35
    if ((35) < yPar < 105): 
      num = 4
      y = 105
    elif ((-35) < yPar < (35)): 
      num = 5
      y = 35
    elif (-105 < yPar < (-35)):
      num = 6
      y = -35
    addToMoveList(num, moveList, play1Moves, play2Moves)
  if ((35) < xPar < 105):
    x = 35
    if ((35) < yPar < 105): 
      num = 7
      y = 105
    elif ((-35) < yPar < (35)): 
      num = 8
      y = 35
    elif (-105 < yPar < (-35)): 
      num = 9
      y = -35
    addToMoveList(num, moveList, play1Moves, play2Moves)
  
  
trtl.onscreenclick(buttonClick, 1)
trtl.listen
class Button:
  def __init__(cor1, cor2):
    

wn = trtl.Screen()
wn.mainloop()