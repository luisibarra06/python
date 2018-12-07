# plot-dictionary.py
import turtle 

def main():
    #table is a dictionary
    table = {-100:5, -90:10, -80:15, -70:20, -60:25, -50:30,
                -40:35, -30:40, -20:45, -10:50, 0:55,
                    10:60, 20:65, 30:70, 40:75, 50:80,
                    60:85, 70:90, 80:95, 90:100, 100:105
            }
    print(" KEYS ")
    print(table.keys())
    print(" VALUES ")
    print(table.values())
    #turtle graphics
    twin = turtle.Screen()
    twin.clear()
    t = turtle.Turtle()
    #tWin = turtle.Screen()
    for h,k in table.items(): #get the items in the dictionary
        print(h, k) # trace code
        #x,y = table[n]
        t.penup()
        t.goto(h,k)
        t.pendown()
        t.circle(5)
    twin.exitonclick()

main()
