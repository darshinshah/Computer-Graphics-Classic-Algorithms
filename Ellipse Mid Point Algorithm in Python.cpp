from graphics import *
import time

def DrawEllipse(R1,R2):
    global p2
    x = 0
    y = R2
    r1 = R1*R1
    r2= R2*R2
    p1 = r2-(r1*R2) + (r1/4)

    win = GraphWin('Ellipse Drawing Algorithm', 800, 800)

    while (2*r2*x)>=(2*r1*y):
        time.sleep(0.01)
        PutEllipse(win,x,y)
        if p1<0:
            x = x + 1
            p1 = p1 + (2*r2*x) + r2
        else:
            x = x + 1
            y = y - 1
            p1 = p1 + (2*r2*x) - (2*r1*y) + r2

    xsv = (x+(1/2))*(x+(1/2))
    xsy = (y - 1)*(y - 1)
    p2 = r2 * xsv + r1 * xsy - (r1 * r2)

    while y>=0:
        time.sleep(0.01)
        PutEllipse(win, x, y)
        if p2 > 0:
            y = y - 1
            p2 = p2 - 2 * r1 * y + r1
        else:
            y = y - 1
            x = x + 1
            p2 = p2 + (2 * r2 * x) - (2 * r1 * y) + r1


def PutEllipse(win, x, y):
    pt = Point(x+400, y+400)
    pt.draw(win)
    pt = Point(x+400, -y+400)
    pt.draw(win)
    pt = Point(-x+400, y+400)
    pt.draw(win)
    pt = Point(-x+400, -y+400)
    pt.draw(win)


def main():
    R1 = int(input("Enter Radius A :"))
    R2 = int(input("Enter Radius B :"))
    DrawEllipse(R1,R2)
    time.sleep(100)


if __name__ == "__main__":
    main()
