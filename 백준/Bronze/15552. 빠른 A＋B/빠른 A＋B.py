import sys

count = int(sys.stdin.readline().rstrip())

for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(a+b) + '\n')