A = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]
    ]
def distance(point1, point2):
    x1 = point1[0]; x2 = point2[0]
    y1 = point1[1]; y2 = point2[0]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
point1 = [2,0]
point2 = [2,4]
center = [(point1[0] + point2[0]) // 2, (point1[1] + point2[1]) // 2]
radius = distance(point1, center)
for i in range(len(A)):
    for j in range(len(A[0])):
        if distance([i, j], center) <= radius:
            A[i][j] = 1
for row in A:
    print(row)
