def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


points = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))
paths = []
results = []
for first_point in points[1::1]:
    first_step = calculate_distance(points[0][0], points[0][1], first_point[0], first_point[1])
    for second_point in points[1::1]:
        if second_point == first_point:
            continue
        second_step = calculate_distance(first_point[0], first_point[1], second_point[0], second_point[1])
        for third_point in points[1::1]:
            if third_point in (second_point, first_point):
                continue
            third_step = calculate_distance(second_point[0], second_point[1], third_point[0], third_point[1])
            for fourth_point in points[1::1]:
                if fourth_point in (third_point, second_point, first_point):
                    continue
                fourth_step = calculate_distance(third_point[0], third_point[1], fourth_point[0], fourth_point[1])
                fifth_step = calculate_distance(fourth_point[0], fourth_point[1], points[0][0], points[0][1])
                path_length = first_step + second_step + third_step + fourth_step + fifth_step
                result = f"{points[0]} -> {first_point}[{first_step}] -> {second_point}[{first_step + second_step}]\
-> {third_point}[{first_step + second_step + third_step}]\
-> {fourth_point}[{first_step + second_step + third_step + fourth_step}]\
-> {points[0]}[{path_length}] = {path_length}"
                paths.append(path_length)
                results.append(result)
print(results[paths.index(min(paths))])