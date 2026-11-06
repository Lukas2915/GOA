#2
num = [1, 2, 3, 4, 5]
print (num[0])
print (num[-1])
print (num[2])

for  i in (num) :
    print(i)
print()
print()

num1 = int(input("please enter the first number :  "))
print()
if num1 in num :
    print("this number are in the list!")
else :
    print("this number aren't in the list!")
    

#3
ana = 70
niko = 65
vasya = 35
keso = 97
simba = 67
lilo = 90

total_point = [ana, niko, vasya, keso, simba, lilo]
print("the total number of points for the students is", total_point)

no_50less = 0
ye_50more = 0

for point in total_point:
    print(point)

    if point >= 50:
        ye_50more += 1
    else:
        no_50less+= 1

print("scored less than 50 have ", no_50less) 
print("scored more than 50 have ", ye_50more)


#4
num1 = int(input("Please enter your first number  "))
num2 = int(input("Please enter your second number  "))
num3 = int(input("Please enter your third number  "))
num4 = int(input("Please enter your fourth number  "))
num5 = int(input("Please enter your fifth number  "))
num6 = int(input("Please enter your sixth number  "))
num7 = int(input("Please enter your seventh number  "))

numlist = [num1, num2, num3, num4, num5, num6, num7]
print ("numbers list are : ", numlist)

positive = 0
negative = 0
zero = 0

for number in numlist :
    if number > 0 :
        positive += 1
    elif number < 0 :
        negative += 1
    else :
        zero += 1
bignumnum = numlist[0]

for number in numlist:
    if number > bignumnum:
        bignumnum = number
print(f"""
     positive number's are :  {positive} 
     negative number's are :  {negative}
     zero number's are :  {zero} 
     
     the biggest number are ", {bignumnum}
     """)

#5
film1= "Titanic"
film2= "Interstellar"
film3= "The Shawshank Redemption"
filmlist =[film1, film2, film3,]

film4 = input("Please enter your favorite film :  ")
print ( )
filmlist.append(film4)

for i in filmlist :
    print(i)
    

# რა არის .append() :

# Python-ში მეთოდი .append() გამოიყენება სიის (list) ბოლოში ახალი
# ელემენტის დასამატებლად. ის პირდაპირ ცვლის არსებულ სიას და ზრდის მის სიგრძეს ერთით.
# აი მარტივი მაგალითი:
# python
# # ვქმნით საწყის სიას
# ხილის_სია = ["ვაშლი", "ბანანი"]

# # ვამატებთ ახალ ელემენტს ბოლოში
# ხილის_სია.append("ატამი")

# # ვბეჭდავთ შედეგს
# print(ხილის_სია)
# # შედეგი: ['ვაშლი', 'ბანანი', 'ატამი']