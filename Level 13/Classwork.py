# 1
h = int(input("Please enter number: "))

for i in range(h, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
#2
h = int(input("Please enter h: "))

for i in range(1, h + 1):
    print(" " * (h - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
    
    
#3
h = int(input("Введите h: "))

for i in range(1, h + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == h:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#4
h = int(input("INPUT YOUR NUMBER!  "))

for i in range(1, h + 1):
    for j in range(h - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()