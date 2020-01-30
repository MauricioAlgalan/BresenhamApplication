# uncompyle6 version 3.6.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
# [GCC 8.3.0]
# Embedded file name: /home/black/Source/Simulador/Archivo3.py
# Compiled at: 2014-04-23 17:44:19


def get_line(x1=100, y1=100, x2=300, y2=300):
    points = []
    issteep = abs(y2 - y1) > abs(x2 - x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2 - y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax

    if rev:
        points.reverse()
    return points


def circle(radius=50, cc=(100, 100)):
    switch = 3 - 2 * radius
    points = []
    octante1 = []
    octante2 = []
    octante3 = []
    octante4 = []
    octante5 = []
    octante6 = []
    octante7 = []
    octante8 = []
    x = 0
    y = radius
    while x <= y:
        octante1.append((x + cc[0], -y + cc[1]))
        octante2.append((y + cc[0], -x + cc[1]))
        octante3.append((y + cc[0], x + cc[1]))
        octante4.append((x + cc[0], y + cc[1]))
        octante5.append((-x + cc[0], y + cc[1]))
        octante6.append((-y + cc[0], x + cc[1]))
        octante7.append((-y + cc[0], -x + cc[1]))
        octante8.append((-x + cc[0], -y + cc[1]))
        if switch < 0:
            switch = switch + 4 * x + 6
        else:
            switch = switch + 4 * (x - y) + 10
            y = y - 1
        x = x + 1

    points = octante1 + sorted(octante2) + octante3 + sorted(octante4, reverse=True) + octante5 + sorted(octante6, reverse=True) + octante7 + sorted(octante8)
    return points
# okay decompiling Archivo3.pyc
