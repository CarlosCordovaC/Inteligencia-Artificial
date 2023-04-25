# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:15:49 2023

búsqueda informada (heurística)
@author: carlo
"""

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def heuristic(node1, node2):
    return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5

def astar(start, goal, graph):
    open_set = set([start])
    closed_set = set()
    while open_set:
        current = min(open_set, key=lambda node: node.f)
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        open_set.remove(current)
        closed_set.add(current)
        for neighbor in graph[current]:
            if neighbor in closed_set:
                continue
            tentative_g = current.g + heuristic(current, neighbor)
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g >= neighbor.g:
                continue
            neighbor.parent = current
            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
    return None

graph = {
    Node(0, 0): [Node(0, 1), Node(1, 0)],
    Node(0, 1): [Node(0, 0), Node(0, 2)],
    Node(0, 2): [Node(0, 1), Node(1, 2), Node(0, 3)],
    Node(0, 3): [Node(0, 2), Node(1, 3)],
    Node(1, 0): [Node(0, 0), Node(2, 0)],
    Node(1, 2): [Node(0, 2), Node(2, 2), Node(1, 3)],
    Node(1, 3): [Node(0, 3), Node(1, 2)],
    Node(2, 0): [Node(1, 0), Node(3, 0), Node(2, 1)],
    Node(2, 1): [Node(2, 0), Node(2, 2), Node(3, 1)],
    Node(2, 2): [Node(1, 2), Node(2, 1), Node(2, 3)],
    Node(2, 3): [Node(2, 0),   Node(2, 2), Node(3, 3)],
    Node(3, 0): [Node(2, 0), Node(3, 1)],
    Node(3, 1): [Node(2, 1), Node(3, 0), Node(3, 2)],
    Node(3, 2): [Node(3, 1), Node(3, 3)],
    Node(3, 3): [Node(2, 2), Node(3, 2)]
}

start = Node(0, 0)
goal = Node(3, 3)

path = astar(start, goal, graph)

if path:
    for node in path:
        print(f"({node.x}, {node.y}) -> ", end="")
    else:
         print("No solution found.")
