import sys

count = int(sys.stdin.readline().rstrip())

for i in range(1, count+1):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write('Case #' + str(i) + ': ' + str(a+b) + '\n')