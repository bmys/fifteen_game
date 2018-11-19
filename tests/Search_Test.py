import unittest
from state import State
from search.bfs import BFS
from search.dfs import DFS

from program import load_puzzle

import numpy as np
from collections import OrderedDict
import time

class BFSTest(unittest.TestCase):

    # def test_first_state_correct(self):
    #     state_array = np.array([
    #         [1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 0]])
    #     bfs = BFS(state_array)
    #     self.assertEqual(bfs.search(), '')
    #
    # def test_search(self):
    #     state_array = np.array([
    #         [1, 2, 3],
    #         [4, 5, 0],
    #         [7, 8, 6]])
    #     bfs = BFS(state_array)
    #     self.assertEqual(bfs.search(), 'D')
    #
    # def test_dict(self):
    #     a = OrderedDict()
    #     a['foo'] = 5
    #     a['bar'] = 3
    #     # print(a.popitem())
    #     print(a)
    #     for i in a:
    #         print(i)
    #
    #     b = iter(a)
    #     print(b.__next__())


    # GOOOOD
    # def test_search2(self):
    #     # state_array = np.array([
    #     #     [1, 2, 3],
    #     #     [4, 5, 6],
    #     #     [7, 8, 8]])
    #     start_time = time.perf_counter()
    #
    #     state_array = np.array(
    #     [
    #     [6, 0, 2, 3],
    #     [9, 5, 7, 4],
    #     [10, 1, 11, 8],
    #     [13, 14, 15, 12]
    #     ])
    #
    #     # state_array = np.array(
    #     #     [
    #     #         [1, 2, 3, 4],
    #     #         [5, 6, 11, 7],
    #     #         [0, 9, 10, 8],
    #     #         [13, 14, 15, 12]
    #     #     ])
    #
    #     # state_array = np.array(
    #     #     [
    #     #         [1, 3, 4, 0],
    #     #         [5, 2, 7, 8],
    #     #         [9, 6, 10, 11],
    #     #         [13, 14, 15, 12]
    #     #     ])
    #
    #     # [
    #     # [6, 0, 2,3],
    #     # [9,5,7,4],
    #     # [10,1,11,8]
    #     # [13,14,15,12]
    #     # ]
    #     bfs = BFS(state_array)
    #     path = bfs.search()
    #     endtime = time.perf_counter()
    #
    #     print('Time: %s' % str(endtime - start_time))
    #     print('Path %s' % path)

    def test_search5(self):
        # state_array = np.array([
        #     [1, 2, 3],
        #     [4, 0, 5],
        #     [7, 8, 6]])

        # state_array = np.array([
        #     [1, 5, 2],
        #     [7, 4, 3],
        #     [0, 8, 6]], dtype=np.uint8)

        # state_array = np.array([
        #     [1, 5, 2],
        #     [4, 8, 3],
        #     [7, 0, 6]], dtype=np.uint8)

        # state_array = np.array([
        #     [4, 1, 3],
        #     [7, 2, 6],
        #     [5, 0, 8]], dtype=np.uint8)


        # state_array = np.array(
        #     [
        #     [5, 1, 3,  4],
        #     [0,2, 6,   8],
        #     [9, 10, 7, 11],
        #     [13, 14, 15, 12]
        #     ],dtype=np.uint8)
        #

        # state_array = np.array(
        # [
        # [6, 0, 2, 3],
        # [9, 5, 7, 4],
        # [10, 1, 11, 8],
        # [13, 14, 15, 12]
        # ])

        # state_array = np.array(
        # [
        # [1, 0, 2,  4],
        # [5, 6, 3,  7],
        # [9, 10, 11,8],
        # [13, 14, 15, 12]
        # ])

        # state_array = np.array(
        # [
        # [1, 3, 4,  0],
        # [5, 2,  6, 8],
        # [9, 10, 7, 12],
        # [13, 14, 11, 15]
        # ])

        # state_array = np.array(
        # [
        # [1, 2, 0,  3],
        # [5, 6,  7, 4],
        # [9, 10,11, 8],
        # [13, 14, 15, 12 ]
        # ])

        state_array = load_puzzle('../puzzles/4x4_07_00002.txt')
        start_time = time.perf_counter()

        dfs = DFS(state_array, ['L', 'R', 'U', 'D'])
        path = dfs.search()
        endtime = time.perf_counter()

        print('Time: %s' % str(endtime - start_time))
        print('Path %s' % path)

    # def test_search2(self):
    #     # state_array = np.array([
    #     #     [1, 0, 2],
    #     #     [4, 5, 3],
    #     #     [7, 8, 6]])
    #
    #     state_array = np.array([
    #         [1, 5, 2],
    #         [7, 4, 3],
    #         [0, 8, 6]], dtype=np.uint8)
    #
    #     start_time = time.perf_counter()
    #
    #     dfs = DFS(state_array)
    #     path = dfs.search()
    #     endtime = time.perf_counter()
    #
    #     print('Time: %s' % str(endtime - start_time))
    #     print('Path %s' % path)
    #
    #
    #