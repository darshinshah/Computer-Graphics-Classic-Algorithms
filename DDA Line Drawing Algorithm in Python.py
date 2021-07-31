from graphics import *
import time

def DAA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = float(dy) / float(dx)
    win = GraphWin('DAA Line', 600, 600)
    if slope > 1:
        temp1 = x1
        for i in range(y1,y2):
            PutPixle(win, temp1, i)
            temp1 = temp1 + (1 / slope)
            time.sleep(0.01)
    else:
        #print("hi")
        temp2 = y1
        for i in range(x1, x2):
            PutPixle(win, temp2, i)
            temp2 = temp2 + slope
            time.sleep(0.1)
def PutPixle(win, x, y):
    pt = Point(x, y)
    pt.draw(win)
def main():
    x1, y1, x2, y2 = input('Enter x1, y1, x2, y2 separated by space:').split()
    x1, y1, x2, y2 = [int(x) for x in [x1, y1, x2, y2]]
    '''x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))'''
    DAA(x1, y1, x2, y2)
if __name__ == "__main__":
    main()