# # 1 davaleba
# num = int (input('Please enter your full number '))
# if num > 0 :
#     print ('Your number is positive')
# elif num < 0 :
#     print ('Your number is negative')
# else :
#     print ('Your number is zero')
# if num % 2 == 0 :
#     print ("Your number is even")
# else :
#     print ("Your number is odd")
    
# # 2 davaleba
# num_ss = 67
# popitka = 0

# while True:
#     num_input = int (input('Please enter correct number '))
#     popitka += 1 
#     if num_input > num_ss :
#         print ( f"{num_input } > secret" )
#     elif num_input < num_ss :
#         print ( f"{num_input } < secret" )
#     else : 
#         break
# print ('Your number is correct')
# print (f"{num_input} = {num_ss}")        
# print (f"You made {popitka} attempts")

#3 davaleba
# total = 0
# product = 0

# while True:
#     name = input("product name :  ")
#     print("if you want break, enter num - zero (0)")

#     if name == "0":
#         break

#     price = float(input("price:"))
#     quantity = int(input("quantity: "))

#     total_sum = price * quantity
#     total = total + total_sum

#     product.append((name, price, quantity, total_sum))  
#     print(f"add: {name} - {total_sum} GEL")
#     print(f"Current price: {total} GEL")

# # cheki
# print("\n===== Chek =====")
# for name, price, quantity, item_total in product:
#     print(f"{name}: {price:.2f} x {quantity} = {item_total:.2f} GEL")

# print("-----------------")
# print(f"full pay: {total:.2f} GEL")
# print("-----------------")


#davaleba 4

# tickets = 0
# ticket_price = 0
# procent = 0

# total_tickets = 0 #biletebis full raodenoba
# total_original = 0 #biletebis sacxisi pasebi
# total_discount = 0 # pasdakleba
# total_payment = 0 #gadasaxadebi

# while True:
#     age = int(input("Please enter your age: "))

#     if age < 0:
#         print("Incorrect age! Try again!")
#         continue

#     tickets = int(input("Enter tickets quantity: "))

#     if tickets < 0:
#         print("Please enter correct ticket quantity!")
#         continue
#     elif tickets == 0:
#         print("You need minimum 1 ticket!")
#         continue

#     if age < 12:
#         ticket_price = 10
#     elif age >= 60:
#         ticket_price = 12
#     else:
#         ticket_price = 15

#     # biletebis jami
#     original_num = ticket_price * tickets

#     # pasdaklebis procenti
#     if tickets >= 5:
#         procent = 0.20
#     elif tickets >= 3:
#         procent = 0.10
#     else:
#         procent = 0

#     # pasdakleba da samoloo xirebuleba
#     discount = original_num * procent
#     payment = original_num - discount

#     # full plus monacemebis
#     total_tickets += tickets
#     total_original += original_num
#     total_discount += discount
#     total_payment += payment

#     print("Original price:", original_num, "GEL")
#     print("Discount:", discount, "GEL")
#     print("Final price:", payment, "GEL")

#     answer = input("do you want to buy more tickets? (yes/no): ")

#     if answer != "yes":
#         break

# # total angarishis
# print("--- total---")
# print("Total tickets:", total_tickets)
# print("Original price:", total_original, "GEL")
# print("Total discount:", total_discount, "GEL")
# print("Final payment:", total_payment, "GEL")
# .

#5 davaleba (wweell well well...)

balance = float(500)
successful_operations = 0

count = 0

while True :
    print( """ 
------------------------------
-----Welcom to STar Bank!----- 
1.   1 - Balance view
2.   2 - Deposit money
3.   3 - Withdraw money
4.   4 - transactions
5.   5 - EXIT 
------------------------------""")
    
    choice = input("select number :  ")
    if choice == "1" :
        print (f"your balance is :  {balance}")
    elif choice == "2":
        deposit = float(input("please enter deposit money :  "))
        if deposit <= 0 :
            print ("please enter correct number!")
            continue 
        else:
            balance += deposit
            print(f"Your new balance is: {balance}")
            successful_operations += 1
            
    elif choice == "3":
        takeofmoney = float(input("How much money do you want to take out? : "))

        if takeofmoney <= 0:
            print("ERROR! Please enter a positive number!")
            continue

        elif takeofmoney > balance:
            print("ERROR! Insufficient balance!")
            continue

        else:
            balance -= takeofmoney
            print(f"Your new balance is: {balance}")
            successful_operations += 1
    
    elif choice == "4":
        print(f"your number of successful operations: {successful_operations}")
    elif choice == "5" :
        break
        