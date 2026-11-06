
total = 0
product = 0
while True :
    print ("if you want come back, enter /228 ")
    name = input("please enter product name :  ")
    if name == "228" :
        break
    
    quantity = int(input(f"enter quantity of, {name} "))
    price = float(input(f"enter price of, {name}"))
    
    total_sum = quantity * price 
    total = total + total_sum
    print("====================")
    print(f"product : {name}")
    print(f"quantity : {quantity}")
    print(f"product price : {price}")
    print("====================")
        
    #თუ თქვენ კითხულობთ დავალებას 3, მე ან ვერ გავიგე ან დამავიწყდა მისი მორჩენა..
    
    