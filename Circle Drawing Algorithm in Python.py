from graphics import *
import time


def Midpoint(R):
    x = 0
    y = R
    h = 1 - R
    dE = 3
    dSE = -2*(R) + 5
    win = GraphWin('Midpoint Circle Algorithm', 600, 480)
    PutCircle(win, x, y)
    while y > x:
        if h < 0:
            h = h + dE
            dE = dE + 2
            dSE = dSE + 2
        else:
            h = h + dSE
            dE = dE + 2
            dSE = dSE + 4
            y = y - 1
        x = x + 1
        # delay for 0.01 secs
        time.sleep(0.01)
        PutCircle(win, x, y)


def PutCircle(win, x, y):
    pt = Point(x+200, y+200)
    pt.draw(win)
    pt = Point(x+200, -y+200)
    pt.draw(win)
    pt = Point(-x+200, y+200)
    pt.draw(win)
    pt = Point(-x+200, -y+200)
    pt.draw(win)
    pt = Point(y+200, x+200)
    pt.draw(win)
    pt = Point(y+200, -x+200)
    pt.draw(win)
    pt = Point(-y+200, x+200)
    pt.draw(win)
    pt = Point(-y+200, -x+200)
    pt.draw(win)


def main():
    R = int(input("Enter Radius "))
    Midpoint(R)


if __name__ == "__main__":
    main()