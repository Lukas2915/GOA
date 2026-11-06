
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
sum=0

for i in num :
    sum += num ** 2
print ("Sum of squares are", sum) 

num=[3, 7, 12, 5, 22, 9, 11, 4, 21, 13, 16]
even_sum = 0
odd_suum= 0
for i in num :
    if num % 2 == 0 :
        even_sum += 0
    else:
        odd_suum += 0
print ("even number's are", even_sum)
print ("odd numbe's are", odd_suum)


count = int(input("enter your  num"))

number = []
for i in range(count) :
    num=int(input(f"Enter {i + 1}-num"))
    number.append(num)
print("your numbers are", num)

maximum = number[0]
minimum = number[0]

for i in range(1, count):
    if number[i] > maximum:
        max = number[i]

    if number[i] < minimum:
        min = number[i]
        
print("Maximum", max)
print("Minimum", min)


# nn= 0
# n = int(input("enter student's number"))
# score = []

# for i in range(n) :
#     while True:
#         score = int(input("input student's score"1))
#         if 0 <= score <=100 :
#             score.append(score)
#         else :
#             print("ERROR! enter score from 1 to 100")
#         continue 
# nn = score.append / score

# passed =0
# failed = 0
# for score.append in score :
#     if score > 60 :
#         passed += 1
#     elif score < 60 :
#         failed +=1