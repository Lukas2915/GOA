#2 მე გადავწყვიტე გამეკეთებინა უფრო საინტერესო მეთოდით
product_list = ['apple', 'bread', 'milk', 'potato']
product = []
delete = []
while True :
    print("""
            """)
    print("""
        ~=~=~=~=~=Shop=~=~=~=~=~=
        Choice 1 -> view list
        Choice 2 -> add product
        Choice 3 -> EXIT
        ~=~=~=~=~=~=~=~=~=~=~=~=~   
          """)
    choice = int(input("Please enter valid number :  "))
    if choice == 1 :
        print("Product list : ", product_list)
    elif choice == 2 :
        print()
        product = input("What product you want add?  ")
        product_list.append(product)
        print(product_list)
    elif choice == 3 :
        print()
        print("Bye !")
        break
    else :
        print("Number is invalid")
        
#3 
name_list = ["Luka", "Gio", "Timur", "Petre", "Natia"]
print(" student name list (Original): ", name_list)

name_list.sort()
print("Student name list (sort): ", name_list)

#4
animals = ["Elephant", "Lion", "Panda", "Tiger", "Monkey 'Po'", "Monkey 'Li'", "Hipopotamus"]
name = []
animals.sort()
while True :
    print()
    print("Zoo, animals list : ",animals)
    print("Choice 1 --> View list")
    print("Choice 2 --> Remove animal")
    print("Choice 3 --> Add new animal")
    print("Choice 4 --> EXIT")
        
    choice = int(input("Enter valid number :  "))
    if choice == 1 :
        print(animals)
        print()
    elif choice == 2 :
        name = input("Input name for remove animal from list :  ")
        animals.remove(name)
        print()
    elif choice == 3 :
        name = input("Input name for add animal to list :  ")
        animals.append(name)
        print()
    elif choice == 4 :
        print("Byebye! thanks for visiting!")
        break
    else :
        print("Invalid number, try again")

#5  
num_list = [ 123, 245, 345, 456, 567]
print("Original number list : ", num_list)

num_list.pop(-1)
print("Deleted number at index '-1' : ", num_list)

num_list.insert(5, 678)
print("Inserted number '678' with index '5' : ", num_list)

num_list.reverse()
print("Reversed list : ", num_list)
