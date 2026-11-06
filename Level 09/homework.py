#p.s разбирался
# sum = 0
# i = 0
# while i <= 10:
#     sum += i
#     i += 1
# print(f"{sum} X {i} = {sum * i}")
    
num = int(input("Please enter your number:  "))
if num > 0 :
    print("your number is positive")
elif num < 0 :
    print("your number is negative")
elif num == 0 :
    print ("your number is 0? you are seriously?")
    
score = int(input("please enter your score from 1 to 100:  "))
if score >= 90 and score <= 100 :
    print("well done, you got an A!")
elif score < 0 and score > 100 :
    print ("no no no, enter your score from 1 TO 100!!!!")
elif score >= 80 and score <= 89 :
    print("Nice, you got an B!")
elif score >= 70 and score <79 :
    print("Not bad, you got an C!")
elif score >= 60 and score <= 69 :
    print ("You can more! you got an D!")
elif score >= 0 and score < 59 :
    print ("Bad.. try again. you got an F!")
    
    
sub = 67
subb = int(input("please enter correct number:  "))
while sub != subb :
    print ("PLEASE ENTER CORRECT NUMBER!")
    subb = int(input("please enter correct number:  "))
print (" yeye 67 67 67")
print ("You guessed the number!") 
  
num1 = float(input("Well, please enter first number:  "))
num2 = float(input("also enter second number:  "))
print ("+ was ", num1 + num2)
print ("- was ",num1 - num2)
print ("* was ",num1 * num2)
print ("% was ",num1 % num2)
print ("/ was ",num1 / num2)
print ("// was ",num1 // num2)



# p.s разбирался 
# name = input("Please, enter your name: ")
# correct_password = str(12345678)
# password_input = int(input("Please enter your password:  "))

# if correct_password <= 8 :