# 1) შექმენით პროგრამა რომელიც while ციკლის მეშვეობით დაბეჭდავს თქვენს სახელს 5 ჯერ
# i = 0
# while i < 5 :
#     print("Lukas")
#     i += 1
    
# 2) შექმენით პროგრამა რომლითაც დაითვლით 0დან 10ის ჩათვლით რიცხვთა ჯამს
sum = 0
i = 0
while i <= 10:
    sum += i
    i += 1
print(f"{sum} X {i} = {sum * i}")
    
# 3) მომხმარებელს შემოატანინეთ რიცხვი თქვენი დავალებაა ნულიდან მაგ რიცხვის ჩათვლით გამოთვალოთ 
# მხოლოდ ლუწების ჯამი (გამოიყტენეთ whle ციკლი არანაირი if-else არ გჭირდებათ)

number=int(input("ENter number "))

sum1 = 0
sum2 = 2
while sum2 <= number:
     sum1 += sum2
     sum2 += 2 
print(f'{number}{sum1}')


# 4) შექმენით ცვლადი სახელად saved_password სადაც შეინახავთ 
# თქვენს სასურველ პაროლს მაგალითად "123", 
# შემდეგ მომხმარებელს შემოატანინეთ პაროლი password_input ცვლადში,
# თქვენი დავალებაა მომხმარებელს იქამდე შემოატანინოთ პაროლი 
# *სანამ შემოტანილი პაროლი არ იქნება შენახული პაროლის ტოლი

save_password = "123"

# input() პირდაპირ აბრუნებს ტექსტს, int() აღარ გვჭირდება
password_input = input('Enter new pin password: ')

while password_input != save_password:
    print("password incorrect")
    password_input = input("Please login password pin: ")
print("Password is correct")
    
    
# 5) მომხმარებელს შემოაყვანინეთ თავისი ასაკი, 
# შემდგომ იმ შემთხვევაში თუ მისი ასაკი მეტია 18-ზე
# დაეწერეთ "You are adult!", ყველა სხვა შემთხვევაში დაუწერეთ "You are not adult!".

age = int(input('please enter your age: '))
if age >= 18 :
   print ( ' YOUU ARE ADULT!!! ')
else :
   print (' You are not adult! ')
   
   
# 6) მომხმარებელს შემოაყვანინეთ ერთი რიცხვი, შემდგომ შეამომწეთ,
# იმ შემთხვევაში თუ რიცხვი ლუწია გამოუტანეთ 
# ტერმინალში "Your number is even!" ყველა სხვა შემთხვევაში "Your number is odd!"

num = int(input("Please Enter number: "))
if num % 2 == 0 :
    print("Your number is even!")
else:
    print("Your number is odd!")
    
    
# 7) მომხმარებელს შემოაყვანინეთ სამი რიცხვი,
# თქვენი დავალებაა გაარკვიოთ ამ სამიდან რომელი რიცხვი არის ყველაზე დიდი,
# გამოიყენეთ if, elif და else.

num1 = float(input("first: "))
num2 = float(input("second number: "))
num3 = float(input("therd number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(largest)