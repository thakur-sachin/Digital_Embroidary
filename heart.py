import numpy as np

def generate_heart_shape_points(step=0.05, scale=10):
    points = []
    x_values = np.arange(-1.2, 1.2, step)
    for x in x_values:
        for y in np.arange(-1.2, 1.2, step):
            if (x**2 + y**2 - 1)**3 - x**2 * y**3 <= 0:
                points.append((x, y))
    stitch_points = [(int(x*scale) + 100, int(y*scale) + 100) for x, y in points]
    stitch_points = sorted(stitch_points, key=lambda point: (point[1], -point[0]), reverse=True)
    return stitch_points

def convert_to_stitches(points):
    stitches = [128, 2]
    prev_x, prev_y = points[0]
    for (x, y) in points[1:]:
        dx = x - prev_x
        dy = y - prev_y
        stitches += [dx, dy]
        prev_x, prev_y = x, y
    stitches += [128, 16]
    return stitches

heart_points = generate_heart_shape_points()
heart_stitches = convert_to_stitches(heart_points)

num_stitches = len(heart_stitches) // 2
jef_header = [124, 0, 0, 0, 10, 0, 0, 0] + [ord(c) for c in "202302280000"] + [1, 0, 0, 0, num_stitches & 0xff, (num_stitches >> 8) & 0xff, 0, 0] + [3, 0, 0, 0] + [50]*32 + [2, 0, 0, 0, 13, 0, 0, 0]
jef_bytes = bytes(jef_header + heart_stitches)

with open("heart_shape.jef", "wb") as f:
    f.write(jef_bytes)
