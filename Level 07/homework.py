
name = input("please enter your name :  ")
age = int(input("greate, also enter your age :  "))
if age >= 18 :
    print ("you are adult. welcom!")
elif age < 18 :
    print ("you are not adult. go back!!!!!")

num1 = int(input("please, enter first number : "))
num2 = int(input("please, enter second number :  "))
if num1 < num2 :
    print(num1, "<", num2)
elif num1 > num2 :
    print(num1, ">", num2)
elif num1 == num2 :
    print(num1, "=", num2)
    
    
age = int(input("please enter your age :  "))
c_password =67676767
password = int(input("please enter your password :  "))

if age < 13 :
    print ("Please go back. My coder doesn't know how to stop you from continuing the form, becouse age < 13 :P")
    print (False)
if password == c_password :
    print (True)
if age == True and password == True :
    print (" WELCOME! ")
else :
    print (" GO BACK! ")
    
age = int(input("please enter your age :  "))
price = float(input("enter your product price :  "))

if price >= 100 and age >= 18:
    print("you are adult and you buy this product!")
else:
    print("you aren't adult or you need more money for buy this product!")
if price >= 100 or age >= 18:
    print("you are adult and you buy this product! ")
elif price < 100 or age <= 18 :
    print("you aren't adult, but you buy this product!")
    