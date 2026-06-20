#! /usr/bin/python3

from collections import deque
import pytest
from maze import *

class Test_Maze:
    def _check_connected(self, testMaze):
        # Check if Maze <testMaze> is connected by running
        # DFS starting from (0, 0) and checking that all
        # coordinates are visited.
        unvisited = set()
        for i in range(testMaze.getWidth()):
            for j in range(testMaze.getHeight()):
                unvisited.add((i, j))
        visited = set()
        # DFS
        curr = testMaze.getGraph(0, 0).getSquare()
        stack = deque([curr])
        visited.add(curr.getVertex())
        while len(stack) > 0:
            unvisited.remove(curr.getVertex())
            for square in curr.getNeighbors():
                if square.getVertex() not in visited:
                    stack.append(square)
                    visited.add(square.getVertex())
            curr = stack.pop()
        return len(unvisited) == 0
    def test_setup(self):
        # Check if graph is connected, check if min cycle size
        for w in [2, 7, 12]:
            for h in [2, 7, 12]:
                for minCycle in [4, 8, 12]:
                    testMaze = Maze(w, h)
                    testMaze.setup(minCycle)
                    assert self._check_connected(testMaze), f"Graph not connected after setup: width={w}, height={h}, minCycle={minCycle}"

class Test_DisjointSetUnion:
    def test_union(self):
        dsu = DisjointSetUnion()
