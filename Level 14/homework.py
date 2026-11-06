#2
#ვთხოვე მომხმარებელს მთელი რიცხვის შეტანა და ვაქცევ ინტეჯერად
num = int(input("Please enter positive number :  ")) 
count = 0 #ციფრების ჯამური შემადგენლობა რიცხვში
sum = 0 #ციფრთა ჯამი 
odd = 0
even = 0

while num > 0 : #სანამ რიცხვი მეტია 0-ზე
    digit = num % 10  #პირველი ციფრები = რიცხვი გაყოფილი 10-ზე
    count += 1 # ციფრების ჯამური შემადგენლობა
    if count % 2 == 0 :
        even += 1
    else :
        odd += 1 
    sum += digit # სულ ჯამი რიცხვის ციფრების
    num = num // 10 #რომ ავღნიშნოთ შემდეგი რიცხვის პორველი ციფრი
#პრონტით გამოვყავი ყველა საჭირო ცვლადები
print ("number's count are",count)
print ("total sum are ", sum)
print ("ODD sum  : ", odd)
print ("EVEN sum : ", even ) 

#მერე დამეზარა კმენტარების გაკეთება ХD

#3
number_list = []
largest_num = 0
minimal_num = 0
total = 0

positive = 0
negative = 0
zero = 0
# sum(number_list) складывает все числа в списке
# max(number_list) возвращает самое большое число
# min(number_list) возвращает самое маленькое число
# len(number_list) возвращает количество чисел в списке, Здесь это будет 15.

for i in range(1, 16):
    number = int(input(f"Please enter number {i}: "))
    number_list.append(number)
    if number > 0 :
        positive += 1
    elif number < 0 :
        negative += 1 
    else :
        zero += 1
largest_num = max(number_list) 
minimal_num = min(number_list)
total = sum(number_list)

print("Your list :", number_list)
print("largest number are ", largest_num )
print("min. number are ", minimal_num)
print("total sum are ", total)

print("positive number's are ", positive)
print("negative number's are ", negative)
print("zero number's are ", zero)

#4
password = 37
attempt = 7
miss_attempt = 0
while attempt > 0 :
    input_password = int(input("Enter the correct password :  "))
    if input_password != password :
        if input_password < 37 :
            print("The password is invalid! Your password is shorter than the correct password!")
        elif input_password > 37 :
            print("The password is invalid! Your password is greater than the correct password!")
        attempt -= 1
        miss_attempt += 1
    elif input_password == password :
        "You're Welcome!!"
        break
    
    elif attempt == 0 :
        print("You have no attempts left. Please try again later.")
        break        
print("You are welcome!")
print("You missed", miss_attempt, " attempt's")

#5
first_num = int(input("Please enter fist positive number :  "))
second_num = int(input("Please enter second positive number :  "))
if first_num <=0 or second_num <= 0 :
    print("invalide number, please try again!")
    exit()
fizzbuzz = 0
fizz = 0
buzz = 0
other_numbers = []

for i in range(first_num, second_num + 1):
    if i % 3 == 0 and i % 5 == 0 :
        fizzbuzz += 1
    elif i % 3 == 0 and i % 5 != 0 :
        fizz += 1
    elif i % 3 != 0 and i % 5 == 0 :
        buzz +=1
    else:
         other_numbers.append(i)
print ("number's that are not divisible by 3 and 5", other_numbers)
print(f'''
      You'r list have {fizzbuzz} FizzBuzz
      You'r list have {fizz} Fizz
      You'r list have {buzz} Buzz      
      ''')




# GABEDE DA ASE DACERE CODI ME-3 DAVALEBIS:
# num_list = []

# num1 = int(input("Please enter your 1st number :  "))
# number_list.append(num1)
# num2 = int(input("Please enter your 2st number :  "))
# number_list.append(num2)
# num3 = int(input("Please enter your 3st number :  "))
# number_list.append(num3)
# num4 = int(input("Please enter your 4st number :  "))
# number_list.append(num4)
# num5 = int(input("Please enter your 5st number :  "))
# number_list.append(num5)
# num6 = int(input("Please enter your 6st number :  "))
# number_list.append(num6)
# num7 = int(input("Please enter your 7st number :  "))
# number_list.append(num7)
# num8 = int(input("Please enter your 8st number :  "))
# number_list.append(num8)
# num9 = int(input("Please enter your 9st number :  "))
# number_list.append(num9)
# num10 = int(input("Please enter your 10st number :  "))
# number_list.append(num10)
# num11 = int(input("Please enter your 11st number :  "))
# number_list.append(num11)
# num12 = int(input("Please enter your 12st number :  "))
# number_list.append(num12)
# num13 = int(input("Please enter your 13st number :  "))
# number_list.append(num13)
# num14 = int(input("Please enter your 14st number :  "))
# number_list.append(num14)
# num15 = int(input("Please enter your 15st number :  "))
# number_list.append(num15)

# print(number_list)