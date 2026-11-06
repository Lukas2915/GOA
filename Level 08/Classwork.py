# 1) შექმენით ციკლი რომელიც 0_დან მომხმარებლის მიერ შემოტანილი რიცხვი
# ჩათვლით გამოითვლის ჯამს და საბოლოოდ დაბეჭდეთ ეს ჯამი

number = int(input('Enter your number '))
ladno = 0

for i in range(number + 1) :
    ladno = ladno + 1
print(ladno)

# 2) მომხმარებელს შემოატანინეთ რიცხვი
# თქვენი დავალებაა 0_დან მაგ რიცხვის ჩათვლით ყველა ლუწი რიცხვის ჯამი გამოთვალოთ და დაბეჭდოთ ჯამი

number = int(input("enter yu number: "))
all = 0

for i in range(0, number + 1 , 2):
    all = all + i

print(all)