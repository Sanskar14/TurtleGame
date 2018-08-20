from turtle import *
from random import randint

def Create_Path():
    for row in range(15):
      #t.speed(2)  
      t.write(row,align='center')
      t.right(90)
      for coln in range(10):
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
      t.speed(0)  
      t.penup()
      t.backward(200)
      t.left(90)
      t.forward(20)

def Create_Turtle():
    listColor=['Red','Blue','Green','Yellow']
    m=0
    p=100
    for k in listTurtle:
        k = Turtle()
        k.shape('turtle')
        k.color(listColor[m])
        k.penup()
        k.goto(-160,p)
        p-=30
        k.pendown()
        if m%2==0:
            for turn in range(10):
                k.right(36)
        else:
            for turn in range(10):
                k.left(36)
        listTurtle[m]=k
        m+=1
        
    
def Lets_Race():
    for turn in range(100):
      listTurtle[0].forward(randint(1,5))
      listTurtle[1].forward(randint(1,5))
      listTurtle[2].forward(randint(1,5))
      listTurtle[3].forward(randint(1,5))



t=Turtle()
t.penup()
t.setpos(-150,150)
listTurtle=[1,2,3,4]
Create_Path()
Create_Turtle()
Lets_Race()



