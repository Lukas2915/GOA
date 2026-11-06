#Task 1
age = int(input("please enter your age"))
if age <= 13 :
     print("You are child")
elif age >= 13 and age <= 17 :
     print ("You are Teenager")
elif age >= 18 :
     print ("You are Adult")

# ```age = int(input("Please enter age: "))

# if age < 13:
#     print("Child")
# elif age >= 13 and age < 18:
#     print("Teenager")
# else:
#     print("Adult")```

#Task 2
num = int(input("Please enter positive number :  "))
for i in range(0, num):
    if num % 2 == 0 :
        print ("even")
    else :
        print ("odd")

# number = int(input("Please enter number: "))

# for i in range(1, number + 1):
#     if i % 2 == 0:
#         print(i, "Is even")
#     else:
#         print(i, "Is odd")

password = int("python123")
n_password = int(input("enter your password :  "))
if password != n_password :
    print ("wrong")
else :
    print ("good")
    
correct_password = "python123"
input_password = ""

# while input_password != correct_password:
#     input_password = input("Please enter correct password: ")

#     if input_password == correct_password:
#         print("✅ Access granted!")
#     else:
#         print("❌ Try again!")

# თქვენი დავალებაა დაითალოთ რამდენჯერ შეეშალა მომხმარებელს 
# პაროლი და თუ შეცდომების რაოდენობა გაუტოლდება 3 უნდა შეწყვიტოთ პროგრამა.
password = "1234567890"
error = 0
while error < 3:
    n_password = int(input("Please enter password"))
    if n_password == password :
        print ("Welcome!")
    else :
        error += 1
        print ("wrong password")
    if error == 3 :
        print ("You've made 3 mistakes. Try again later.")

# correct_password = "python123"
# input_password = ""
# tries = 0

# while input_password != correct_password and tries != 3:
#     tries += 1
#     input_password = input("Please enter correct password: ")

#     if input_password == correct_password:
#         print("✅ Access granted!")
#     elif tries == 3:
#         print("You tried 3 times! Blocked")
#     else:
#         print("❌ Try again!")


students = int(input("how many students?"))
failed = 0
pased = 0
for i in range(1, students +1 ) :
    score = int(input(f"student {1} score: "))
    if score < 0 or score > 100 :
        print("invaled score! enter score from 1 to 100!!!!!!!!!")
    if score >= 90 :
        print ("A")
    elif score >= 80 and score <89 :
        print ("B")
    elif score > 70 and score < 79 :
        print ("C")
    elif score > 60 and score < 69 :
        print ("D")
    elif score > 0 and score < 59 :
        print ("Broo... F F F")
    if score >= 60:
        passed += 1 
    else :
        failed += 1
print ("Total passed is ", passed)
print ("Total failed is ", failed)

# students_count = int(input("Please enter students quantity: "))

# for i in range(1, students_count + 1):
#     grade = int(input(f"Please enter {i} student score: "))

#     if grade >= 90 and grade <= 100:
#         print(f"{i} student's score is A")
#     elif grade >= 80 and grade < 90:
#         print(f"{i} student's score is B")
#     elif grade >= 70 and grade < 80:
#         print(f"{i} student's score is C")
#     elif grade >= 60 and grade < 70:
#         print(f"{i} student's score is D")
#     elif grade >= 0 and grade < 60:
#         print(f"{i} student's score is F")
#     else:
#         print("Incorect grade")
#         break


balance = float(500.0)
print ("ATM WITHDRAWAL SYSTEM")
print (f"currect balance : {balance} GEL")

while True :
    ammount = float(input("Enter ammount here :  "))
    if ammount == 0 :
        print ("atm sessia error")
        break
    elif ammount < 0 :
        print ("atm: Invalid ammount")
    elif ammount >= balance :
        print ("print Withdrawal successful!")
        
# balance = 500

# while balance != 0:
#     print("Balance is: ", balance)
#     withdrawl_amount = float(input("Please enter withdrawl money: "))

#     if withdrawl_amount > balance:
#         print("Insufficient funds!") 
#     elif withdrawl_amount <= 0:
#         print("Invalid amount!")
#     else:
#         balance -= withdrawl_amount
#         print("Successfully withdrawl!")



