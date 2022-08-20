import turtle
gongjuren=turtle.Turtle()
def Fibonacci(num):
    if num==1 or num==2:
        return 1
    else:
        return Fibonacci(num-1)+Fibonacci(num-2)
gongjuren.penup()
gongjuren.goto(-100,-200)
gongjuren.pendown()
gongjuren.hideturtle()
def Square(length):
    for i in range(4):
        gongjuren.fd(length)
        gongjuren.lt(90)
def GoldSpiral(num):
    if num==0:
        turtle.done()
    else:
        gongjuren.color("orange")
        Square(5*Fibonacci(num))
        gongjuren.color("blue")
        gongjuren.circle(5*Fibonacci(num),90)
        GoldSpiral(num-1)
GoldSpiral(10)
