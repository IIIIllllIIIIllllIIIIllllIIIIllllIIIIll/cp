#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A, B):
	print(A, B)

T = int(input())

for _ in range(T):
	input()
	A = input().split(' ')
	A = list(map(int, A))
	B = input().split(' ')
	B = list(map(int, B))
	ans(A, B)