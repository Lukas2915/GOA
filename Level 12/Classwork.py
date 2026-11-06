#1
name = input("enter your name :  ")
name_s= input ("enter your surname :  ")
age = int (input ("enter your age :  "))

colour = input("your favourite colour :  ")

user_info=[name, name_s, age]
print (user_info)

#2 
masive = ["lana", "marki", "saba", "luka", "biba", "boba", "povel", "napaleon","kote", "salome"]
masive[2] = "winstone"
masive[6] = "keso"
masive[-2] = "ramzas"
print(masive)

#3
#Python-ში for ციკლის დახმარებით შეგვიძლია List-ში არსებული ყველა ელემენტი რიგ-რიგობით გამოვიტანოთ ტერმინალში.
# for item in list_name:
#     print(item)

for name in masive:
    print(name)