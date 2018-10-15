# ex4b.py lai
import turtle 
w = turtle.Screen()
w.bgcolor("#004d99")
t = turtle.Turtle()
t.color("#ffd11a")

def thepoly(size):
	for i in range(4):
		t.fd(size)
		t.left(90)
		size = size + 5

thepoly(5)
thepoly(10)
thepoly(15)
thepoly(20)
thepoly(25)
thepoly(30)
thepoly(35)
thepoly(40)
thepoly(45)
thepoly(50)
thepoly(55)
thepoly(60)
thepoly(65)
thepoly(70)
thepoly(75)
thepoly(80)
thepoly(85)
holdit = input();
