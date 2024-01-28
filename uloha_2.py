import sys

def validate_input(value):
    try:
        return float(value)
    except ValueError:
        print("Nespravny vstup.")
        sys.exit(1)

def find_midpoint(x1, y1, x2, y2):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return mx, my

def find_line_relation(x1, y1, x2, y2, x3, y3):

    x1, y1, x2, y2, x3, y3 = map(validate_input, [x1, y1, x2, y2, x3, y3])


    if (x1 == x2 == x3) and (y1 == y2 == y3):
        print("Nektere body splyvaji.")
        sys.exit(0)


    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        print("Body lezi na jedne primce.")


        mx, my = find_midpoint(x1, y1, x3, y3)


        if (x2 == mx) and (y2 == my):
            print(f"Prostredni - bod B.")
        elif (x1 == mx) and (y1 == my):
            print(f"Prostredni - bod A.")
        else:
            print(f"Prostredni - bod C.")
    else:
        print("Body nelezi - jedne primce.")


try:
    x1, y1 = input("Bod A:\n").split()
    x2, y2 = input("Bod B:\n").split()
    x3, y3 = input("Bod C:\n").split()
except ValueError:
    print("Nespravny vstup.")
    sys.exit(1)


find_line_relation(x1, y1, x2, y2, x3, y3)
