import sys

input = sys.stdin.readline()
a, b = list(map(int, input.split()))

result = a/b
sys.stdout.write(str(result))