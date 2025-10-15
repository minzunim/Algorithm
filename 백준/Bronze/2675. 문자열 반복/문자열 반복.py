t = int(input())

for i in range(t):
    number, string = input().split()
    new_string = ''
    for s in string:
        new_string += int(number) * s
    print(new_string)
    