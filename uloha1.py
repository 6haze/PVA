import math

def check_point_validity(point, a):
    wall_count = 0
    for coordinate in point:
        if coordinate == 0 or coordinate == a:
            wall_count += 1
        if coordinate < 0 or coordinate > a or (coordinate < 20 and coordinate != 0) or (a - coordinate < 20 and coordinate != a):
            return False
    return wall_count == 1

def calculate_pipe_length(p1, p2, a):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def calculate_hose_length(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def main():
    a = int(input("Rozmer mistnosti:\n"))
    if a <= 0:
        print("Nespravny vstup.")
        return

    point1 = list(map(int, input("Bod #1:\n").split()))
    if not check_point_validity(point1, a):
        print("Nespravny vstup.")
        return

    point2 = list(map(int, input("Bod #2:\n").split()))
    if not check_point_validity(point2, a):
        print("Nespravny vstup.")
        return

    pipe_length = calculate_pipe_length(point1, point2, a)
    hose_length = calculate_hose_length(point1, point2)

    print("Delka potrubi:", pipe_length)
    print("Delka hadice:", hose_length)

if __name__ == "__main__":
    main()
