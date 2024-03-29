# =======================================================================================================================================

# Author: Alicia Durcheva
# Title: Batttleships
# Description: 

# =======================================================================================================================================


from turtle import *

def draw_square(length):
    pendown()
    for i in range(4):
        forward(length)
        left(90)
    penup()
            
def draw_row(length):
    pendown()
    for i in range(10):
        draw_square(length)
        penup()
        forward(length)
        pendown()
    penup()
        
def draw_boxes(length):
    pendown()
    for i in range(10):
        draw_row(length)
        penup()
        backward(length*10)
        right(90)
        forward(length)
        left(90)
        pendown()
    penup()

def draw_letters(length):
    setposition(-225, 250)
    for letter in "ABCDEFGHIJ":
        write(letter, align = "center", font = ("Arial", 25, "bold"))
        forward(length)

def draw_numbers(length):
    setposition(-275, 200)
    right(90)
    for number in "123456789":
        write(number, align = "center", font = ("Arial", 25, "bold"))
        forward(length)
    write("10", align = "center", font = ("Arial", 25, "bold"))

def draw_board(length):
    draw_boxes(length)
    draw_letters(length)
    draw_numbers(length)

penup()       
speed(20)
setposition(-250, 200)
draw_board(50)

exitonclick()