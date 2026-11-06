#1
num = 1081358731876842679427941287148914702407249

while True :
    print("number are", num)
    num1= int(input("plese enter your positive number:  "))
    if num1 < 0 :
        print ("ERROR, please try again!")
        continue
    
    elif num1 > 9 :
        print ("ERROR, please try again!")
        continue
    
    else:
        count = 0
        n = num 

        while n > 0:
            digit = n % 10 
            if digit == num1:
                count += 1     
            n = n // 10         
        print("The digit", num1, "appears", count, "times")
        break 
    
#2
num = int(input("Enter a natural number: "))
factor = 2

while num > 1:
    if num % factor == 0:
        print(factor, end=" ")
        num = num // factor
    else:
        factor += 1
    
#3
max = 100
a=0
b=1

while a < 100 :
    print(a)
    new_num= a + b
    a = b
    b = new_num 
    
4
num = [7, 28, 16, 24, 5, 8, 19, 10]
max = num[0]
min = num[0]

for i in num :
    if i > max :
        max = i
    if i < min :
        min = i
print("minimal number are ", min)
print("maximal number are", max)

#5
num = [1, 2, 3, 4, 5, 6, 7, 8]
na = []
for i in range (len(num) -1, -1, -1):
    na.append(num[i])
print (na)

for i in range (len(num) -1, -1, -1):
    na.append(num[i])
print(na)