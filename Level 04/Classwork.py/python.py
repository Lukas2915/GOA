#1) მომხმარებელს შემოაყვანინეთ 3 დეტალი მასზე: პირველი სახელი, მეორე გვარი და მესამე ასაკი, შემდგომ ტერმინალში ყველაფერი გამოიტანეთ შემდეგი სახით:

# Hello {აქ მომხმარებლის სახელი}!
# User fullname is {აქ მომხამრებლის გვარიც და სახელიც}
# User age is {აქ მომხმარებლის ასაკი}
# საბოლოოდ მთლიანი კოდი დეტალურად ახსენით კომენტარების სახით.

  # მომხმარებელს შემოვაყვანინებთ სახელს გვარი ასაკი
#first_name = input ვთხოვთ სახელის კონსოლში ჩასმას
first_name = input("please enter your first name: ")
#last name = input ვთხოვთ გვარის კონსოლშუ ჩასმას
last_name = input("please enter your last name: ")
#age = input ვთხოვთ ასაკის კონსოლში შეტანას
age = input("please enter your age: ")


  # გამარჯვება
#გავსცეთ კომპიუტერს პრინტის ბრძანება "Hello სახელი"
print("Hello " + first_name) 
#გავსცეთ კომპიუტერს პრინტის ბრძანება "User full name is სახელი გვარი"
print("User full name is " + first_name + " " + last_name)
#გავსცეთ კომპიუტერს პრინტის ბრძანება "User age is ასაკი"
print("User age is " + age)