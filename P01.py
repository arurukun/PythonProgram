# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-l

lis = [12, 23, 64, 25, 6786, 5]

size = len(lis)

first = lis[0]
last = lis[size - 1]

lis[0] = last
lis[size - 1] = first

print(lis)

