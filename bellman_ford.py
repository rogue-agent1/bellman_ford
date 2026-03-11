#!/usr/bin/env python3
"""Bellman-Ford — shortest paths with negative edges, cycle detection."""
import sys

def bellman_ford(n, edges, src):
    dist = [float('inf')] * n; dist[src] = 0
    prev = [None] * n
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; prev[v] = u
    # Check negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, None  # negative cycle
    return dist, prev

def path(prev, dst):
    p = []; v = dst
    while v is not None: p.append(v); v = prev[v]
    return list(reversed(p))

if __name__ == "__main__":
    edges = [(0,1,4),(0,2,5),(1,2,-3),(2,3,4),(3,1,2),(1,3,6)]
    n = 4
    dist, prev = bellman_ford(n, edges, 0)
    if dist:
        print("Bellman-Ford from node 0:")
        for i in range(n):
            p = path(prev, i)
            print(f"  → {i}: dist={dist[i]}, path={p}")
    else:
        print("Negative cycle detected!")
    # With negative cycle
    edges2 = [(0,1,1),(1,2,-1),(2,0,-1)]
    d2, _ = bellman_ford(3, edges2, 0)
    print(f"\nNegative cycle test: {'detected!' if d2 is None else 'none'}")
