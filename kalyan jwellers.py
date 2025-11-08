print("KALYAN JWELLERS")
name = input("enter name : ")
age = int(input("enter age : "))
gender = input("enter gender : ")
product = input("enter product name : ")
product_gram = int(input("enter a product_gram : "))

current_goldprice = 5752
making_charges = 845

print("-------------------------------------------------")

total_goldprice = current_goldprice * product_gram
print(f"total gold price : {total_goldprice}") 

print("--------------------------------------------------------")
total_making = making_charges * product_gram
print(f"total making charges : {total_making} ")

print("----------------------------------------------------------")
gross_amount = total_goldprice + total_making 
print(f"gross amount : {gross_amount}")
purchase = gross_amount

discount = 0  

if gender == 'M':
    if age > 65:
        if purchase >= 21000 and purchase < 31000:                                          
            print("discount is 20%")
            discount = gross_amount * 20/100  
        elif purchase >= 31000 and purchase < 51000: 
            print("discount is 30%")
            discount = gross_amount * 30/100  
        else:
            print("discount is 35%")
            discount = gross_amount * 35/100  
    else:
        if purchase >= 21000 and purchase < 31000:
            print("discount is 10%")
            discount = gross_amount * 10/100  
        elif purchase >= 31000 and purchase < 51000:
            print("discount is 20%")
            discount = gross_amount * 20/100  
        else:
            print("discount is 25%")
            discount = gross_amount * 25/100  
            
elif gender == 'F':
    if age > 65:
        if purchase >= 21000 and purchase < 31000:
            print("discount is 25%")
            discount = gross_amount * 25/100  
        elif purchase >= 31000 and purchase < 51000: 
            print("discount is 35%")  
            discount = gross_amount * 35/100 
        else:
            print("discount is 40%")
            discount = gross_amount * 40/100  
    else:
        if purchase >= 21000 and purchase < 31000:
            print("discount is 15%")
            discount = gross_amount * 15/100  
        elif purchase >= 31000 and purchase < 51000:
            print("discount is 25%")
            discount = gross_amount * 25/100  
        else:
            print("discount is 30%") 
            discount = gross_amount * 30/100    
    
final = purchase - discount
print(f"final price to pay : {final}")

print("----------------------------------------------------------------")
total_net_amount = gross_amount - discount
print(f"total net amount : {total_net_amount}")