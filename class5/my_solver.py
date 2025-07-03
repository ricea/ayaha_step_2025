#!/usr/bin/env python3

import sys
import math
import random as rd

from google_step_tsp.common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)
    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            
    current_city = 0
    unvisited_cities = set(range(1,N))
    tour = [current_city]
    
    # 焼きなまし法
    while unvisited_cities:
        random_rate = rd.random()
        if random_rate >= 0.15:
            next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
        else:
            next_city = rd.choice(list(unvisited_cities))
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
        
    # 2-opt
    while True:
        switch = False
        size = len(tour)
        for i in range(size-2):
            # p1,p2は連続する2点のindex
            p1 = i
            p2 = i + 1
            for j in range(p2+1, size):
                p3 = j
                # p3がリストの1番最後の点の場合ははじめの点を指定
                p4 = (j+1) % size
                
                # 4点で線分を入れ替えた場合に距離が短くなる場合は入れ替える
                l1 = dist[tour[p1]][tour[p2]]
                l2 = dist[tour[p3]][tour[p4]]
                l3 = dist[tour[p1]][tour[p3]]
                l4 = dist[tour[p2]][tour[p4]]
                if l1+l2 > l3+l4:
                    # 点を入れ替え
                    new_path = tour[p2:p3+1]
                    tour[p2:p3+1] = new_path[::-1]
                    switch = True
        if not switch:
            break                     
    return tour 


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
