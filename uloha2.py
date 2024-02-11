def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def midpoint(point1, point2, point3):
    x_mid = point1[0] if (point2[0] <= point1[0] <= point3[0]) or (point3[0] <= point1[0] <= point2[0]) else \
        point2[0] if (point1[0] <= point2[0] <= point3[0]) or (point3[0] <= point2[0] <= point1[0]) else \
        point3[0]
    y_mid = point1[1] if (point2[1] <= point1[1] <= point3[1]) or (point3[1] <= point1[1] <= point2[1]) else \
        point2[1] if (point1[1] <= point2[1] <= point3[1]) or (point3[1] <= point2[1] <= point1[1]) else \
        point3[1]
    return (x_mid, y_mid)

def are_collinear(point1, point2, point3):
    return (point3[1] - point1[1]) * (point2[0] - point1[0]) == (point3[0] - point1[0]) * (point2[1] - point1[1])

def get_input():
    points = []
    for i in range(3):
        point_str = input(f"Bod {chr(65 + i)}:\n").split()
        if len(point_str) != 2 or not all(is_float(coord) for coord in point_str):
            print("Nesprávný vstup.")
            return None
        points.append((float(point_str[0]), float(point_str[1])))
    return points

def get_point_letter(point, points):
    for letter, p in points.items():
        if p == point:
            return letter

def main():
    points = get_input()
    if points is None:
        return

    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        print("Některé body splývají.")
    elif are_collinear(*points):
        print("Body leží na jedné přímce.")
        mid_point = midpoint(*points)
        mid_point_letter = get_point_letter(mid_point, {chr(65 + i): points[i] for i in range(3)})
        print(f"Prostřední je bod {mid_point_letter}.")
    else:
        print("Body neleží na jedné přímce.")

if __name__ == "__main__":
    main()
