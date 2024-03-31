from bisect import bisect_left, bisect_right
import math
from heapq import heappop, heappush, heapify
from collections import defaultdict, deque, Counter
from functools import lru_cache
import sys
# python only
# from math import comb
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def ARR(x, y, k): return [[k for _ in range(y)] for _ in range(x)]