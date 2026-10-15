   # 2)  მომხმარებელს შემოაყვანინეთ თავისი სახელი, ასაკი და სიმაღლე.
#first_name = input ვთხოვთ სახელის კონსოლში ჩასმას
first_name = input("please enter your first name :  ")
#age = input ვთხოვთ ასაკის კონსოლში შეტანას
age = input("please enter your age :  ")
#hight = input ვთხოვთ ასაკის კონსოლში ჩასმას
hight = input("please enter your hight :  ")

#გავსცეთ კომპიუტერს პრინტის ბრძანება "Hello სახელი"
print("Hello " + first_name ) 
#გავსცეთ კომპიუტერს პრინტის ბრძანება "User age is ასაკი"
print("age: " + age)
#გავსცეთ კომპიუტერს პრინტის ბრძანება "Hight "высота""
print("hight: " + hight)


#
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
#
print((number1) + (number2))
print(int(number1) - int(number2))
print(int(number1) * int(number2))
print(int(number1) / int(number2))
print(int(number1) // int(number2))


#
product_name = input("hich product would you like?: ")
price = input("Enter product price: ")
quantity = input("Enter product quantity: ")
total_price = (int(price) * int(quantity))
#
print("Your total price is: ", total_price)


#
#first_name = input ვთხოვთ სახელის კონსოლში ჩასმას
first_name = input("please enter your first name :  ")
grade1 = int(input("Enter subject 1: "))
grade2 = int(input("Enter subject 2: "))
grade3 = int(input("Enter subject 3: "))
average = (grade1 + grade2 + grade3) / 3

print("Name: ", first_name)
print("Grades: ", grade1, grade2, grade3)
print("Average: ", average)