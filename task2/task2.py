from math import sqrt

if __name__ == '__main__':
    path1 = input('Путь до файла с координатами и радиусом окружности: ')
    path2 = input('Путь до файла с координатами точек: ')
    with open(path1) as f:
        xc, yc = f.readline().split()
        xc, yc = float(xc), float(yc)
        r = int(f.readline(2))
    with open(path2) as f:
        points = f.readlines()
    for point in points:
        x = float(point.split()[0])
        y = float(point.split()[1])
        s = sqrt((xc - x) ** 2 + (yc - y) ** 2)
        if s == r:
            print(0)
        elif s < r:
            print(1)
        else:
            print(2)
