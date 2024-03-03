import sys

def parse_input(line):
    try:
        parts = line.strip().split(':')
        coordinates = parts[0].split(',')
        x = float(coordinates[0])
        y = float(coordinates[1])
        name = parts[1].strip()
        return (x, y, name)
    except (IndexError, ValueError):
        return None

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def find_closest_pairs(airplanes):
    min_distance = float('inf')
    closest_pairs = []

    for i in range(len(airplanes)):
        for j in range(i + 1, len(airplanes)):
            dist = calculate_distance(airplanes[i][:2], airplanes[j][:2])
            if dist < min_distance:
                min_distance = dist
                closest_pairs = [(airplanes[i][2], airplanes[j][2])]
            elif dist == min_distance:
                closest_pairs.append((airplanes[i][2], airplanes[j][2]))

    return min_distance, closest_pairs

def main():
    airplanes = []


    for line in sys.stdin:
        if not line.strip():
            break
        airplane = parse_input(line)
        if airplane:
            airplanes.append(airplane)
        else:
            print("Nespravny vstup.")
            return

    if len(airplanes) < 2:
        print("Nespravny vstup.")
        return


    min_distance, closest_pairs = find_closest_pairs(airplanes)


    print(f"Vzdalenost nejblizsich letadel: {min_distance:.6f}")
    if closest_pairs:
        print(f"Nalezenych dvojic: {len(closest_pairs)}")
        for pair in closest_pairs:
            print(f"{pair[0]} - {pair[1]}")
    else:
        print("Nebyly nalezeny žádné páry letadel se stejnou nejkratší vzdáleností.")

if __name__ == "__main__":
    main()
