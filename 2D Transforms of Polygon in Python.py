import matplotlib.pyplot as plt
import math


def translation(list, no):
    tx, ty = input('Enter the shift/translation vectors separated by space for Point ' + ': ').split()
    tx, ty = [int(x) for x in [tx, ty]]

    for i in range(0, no):
        for j in range(0, 2):
            if (j == 0):
                list[i][j] = list[i][j] + tx
            else:
                list[i][j] = list[i][j] + ty

    print(list)
    ptranslate = plt.Polygon(list)
    plt.gca().add_patch(ptranslate)


def rotation(list, no):
    angledegree = int(input('Enter the Angle for Rotation'))
    angleradians = angledegree * (math.pi / 180)

    for i in range(0, no):
        for j in range(0, 2):
            if (j == 0):
                list[i][j] = math.ceil(
                    (list[i][j] * math.cos(angleradians)) - (list[i][j + 1] * math.sin(angleradians)))
            else:
                list[i][j] = math.ceil(
                    (list[i][j - 1] * math.sin(angleradians)) + (list[i][j] * math.cos(angleradians)))

    print(list)
    protate = plt.Polygon(list)
    plt.gca().add_patch(protate)


def reflection(list, no):
    print('Press 1. for Reflection on Origin')
    print('Press 2. for Reflection on X axis')
    print('Press 3. for Reflection on Y axis')
    print('Press 4. for Reflection on X=Y axis')
    print('Press 5. for Reflection on X=-Y axis')

    ch = int(input('Enter Choice : '))

    if ch == 1:
        for i in range(0, no):
            for j in range(0, 2):
                list[i][j] = list[i][j] * -1
    elif ch == 2:
        for i in range(0, no):
            list[i][1] = list[i][1] * -1
    elif ch == 3:
        for i in range(0, no):
            list[i][0] = list[i][0] * -1
    elif ch == 4:
        for i in range(0, no):
            swap = list[i][0]
            list[i][0] = list[i][1]
            list[i][1] = swap
    elif ch == 5:
        for i in range(0, no):
            swap = list[i][0]
            list[i][0] = list[i][1] * -1
            list[i][1] = swap * -1
    else:
        print('Wrong Choice')

    print(list)
    preflect = plt.Polygon(list)
    plt.gca().add_patch(preflect)


def scaling(list, no):
    sx, sy = input('Enter the Scaling Factor vectors separated by space for Point ' + ': ').split()
    sx, sy = [float(x) for x in [sx, sy]]

    for i in range(0, no):
        for j in range(0, 2):
            if (j == 0):
                list[i][j] = math.ceil(list[i][j] * sx)
            else:
                list[i][j] = math.ceil(list[i][j] * sy)

    print(list)

    ptranslate = plt.Polygon(list)
    plt.gca().add_patch(ptranslate)


def shearing(list, no):
    print('Press 1. for Shearing on Positive X Axis')
    print('Press 2. for Shearing on Positive Y Axis')
    print('Press 3. for Shearing on Negative X Axis')
    print('Press 4. for Shearing on Negative Y Axis')

    ch = int(input('Enter Choice : '))

    if ch == 1:
        shear = int(input('Enter Shear Factor : '))
        for i in range(0, no):
            for j in range(0, 2):
                if (j == 0):
                    list[i][j] = list[i][j] + ((shear) * (list[i][j + 1]))
    elif ch == 2:
        shear = int(input('Enter Shear Factor : '))
        for i in range(0, no):
            for j in range(0, 2):
                if (j == 1):
                    list[i][j] = list[i][j] + ((shear) * (list[i][j - 1]))

    elif ch == 3:
        shear = int(input('Enter Shear Factor : '))
        for i in range(0, no):
            for j in range(0, 2):
                if (j == 0):
                    list[i][j] = list[i][j] - ((shear) * (list[i][j + 1]))

    elif ch == 4:
        shear = int(input('Enter Shear Factor : '))
        for i in range(0, no):
            for j in range(0, 2):
                if (j == 1):
                    list[i][j] = list[i][j] - ((shear) * (list[i][j - 1]))

    pshear = plt.Polygon(list)
    plt.gca().add_patch(pshear)


def main():
    plt.axes()

    list = []
    no = int(input('Enter the No of Sides for Polygon '))

    for i in range(0, no):
        x, y = input('Enter x, y separated by space for Point ' + str(i + 1) + ': ').split()
        x, y = [int(x) for x in [x, y]]
        list.append([x, y])
    print(list)

    polygon = plt.Polygon(list)
    plt.gca().add_patch(polygon)

    print('Press 1. Translation')
    print('Press 2. Rotation')
    print('Press 3. Reflection')
    print('Press 4. Scaling')
    print('Press 5. Shearing')

    ch = int(input('Enter Choice : '))

    if ch == 1:
        translation(list, no)
    elif ch == 2:
        rotation(list, no)  # check karna hain sab with rushad
    elif ch == 3:
        reflection(list, no)
    elif ch == 4:
        scaling(list, no)
    elif ch == 5:
        shearing(list, no)
    else:
        print('Wrong Choice !')

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
