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
        if random_rate >= 0.1:
            next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
        else:
            next_city_index = rd.randint(0,len(unvisited_cities)-1)
            next_city = unvisited_cities(next_city_index)
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
