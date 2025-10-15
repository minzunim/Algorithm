t = int(input())

for _ in range(t):
    number, string = input().split()
    for s in string:
        print(int(number) * s, end="")
    print()