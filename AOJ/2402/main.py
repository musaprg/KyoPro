import sys

from heapq import heappop,heappush
from math import sin,cos,pi,sqrt

N,M,L = None,None,None

def main():
    global N,M,L

    while True:
        N,M,L = map(int,input().split())
        if not N and not M and not L:
            return
        M -= 1
        L -= 1

        stars = [tuple(map(int,input().split())) for _ in range(N)]
        
        distances = calc_distance(stars)

        print("{0:.8f}".format(dijkstra(distances)))


def dijkstra(distances):
    global N,M,L
    queue = []
    d = [sys.maxsize]*N
    visited = [False]*N

    d[M] = 0
    heappush(queue, (0,M))

    while len(queue) != 0:
        p = heappop(queue)
        v = p[1]
        if v == L: break
        if visited[v]: continue
        visited[v] = True
        for t in range(N):
            if d[t] > distances[v][t] + p[0]:
                d[t] = p[0] + distances[v][t]
                heappush(queue, (d[t], t))

    return d[L]


def calc_distance(stars):
    global N,M,L

    distances = [[0]*N for _ in range(N)]

    for i,s1 in enumerate(stars):
        for j,s2 in enumerate(stars):
            if i == j:
                continue
            distances[i][j] = distance(s1,s2)
            #print(i,j,distances[i][j])

    return distances


def distance(s1,s2):
    s1_points = []
    s2_points = []

    s1_lines = []
    s2_lines = []

    x,y,a,r = s1
    for n in range(5):
        px = x - r*sin((a+72*n)/180 * pi)
        py = y + r*cos((a+72*n)/180 * pi)
        s1_points.append((px,py))

    x,y,a,r = s2
    for n in range(5):
        px = x - r*sin((a+72*n)/180 * pi)
        py = y + r*cos((a+72*n)/180 * pi)
        s2_points.append((px,py))

    dist = sys.maxsize
    for p1 in s1_points:
        for p2 in s2_points:
            dx = p1[0]-p2[0]
            dy = p1[1]-p2[1]
            dist = min(dist, sqrt(dx*dx+dy*dy))

    return dist



def l_distance(l1,l2):
     

if __name__ == '__main__':
    main()
