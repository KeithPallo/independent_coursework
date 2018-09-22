# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key = lambda x: x[1])
    #print(segments)
    while len(segments) > 0:
        for i in range(0,len(segments)):
            if len(segments) == 0:
                break
            points.append(segments[0][1])
            segments.pop(0)
            segments = included_point(segments,points,i)

    return points

def included_point(segments,points,index):
    remaining = []

    for x in range(0, len(segments)):
        if len(segments) == 0:
            break
        elif segments[x][0] <= points[index] and segments[x][1] >= points[index]:
            pass
        else:
            remaining.append(segments[x])

    return remaining




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
