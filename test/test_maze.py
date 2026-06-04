#! /usr/bin/python3

import pytest
from maze import *

class Test_Maze:
    def test_setup(self):
        testMaze = Maze(10, 10)
        testMaze.setup(6)
        # Check if graph is connected:
        # Check if min cycle size:
        # - Run DFS on graph starting on each node, add nodes to set,
        # check if size of set is equal to w*h, append cnt if hits a cycle
        # - Repeat for w=2, 7, 12, height=2, 7, 12, min cycle=4,8,12
        # - check if no cnt in list exceeds min cycle

class Test_DisjointSetUnion:
    def test_union(self):
        dsu = DisjointSetUnion()
