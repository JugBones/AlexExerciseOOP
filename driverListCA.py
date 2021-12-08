#calling or importing class module (shopList.py as my class)
from shopListCA import shopListMe

#default function to made a list
def ShopListloop():
    li = []
    count = 0
    
    #loop
    while count < 1:
        count = int(input("How many items do you want to buy, bro? >> "))
        if (count < 1):
            print("Number of your food item must be at least 1, fellas! ")
    
    for i in range(count):
        print(f"Item #{i+1}-")
        name_food = str(input("Name of food you want: "))
        amount_food = 0
        while amount_food <= 0:
            amount_food = float(input("Enter amount of pounds: "))
            if amount_food <=0 :
                 print('Oooopss, please at least you have an amount of your food!!')   
         
        li.append(shopListMe(name_food, amount_food))
        
    return li

#Show the summary of the item that have been purchased
def ShowList(yourlist):
    print("Here's a summary of the items purchased: \n")
    for shopListMe in yourlist:
        print(f"Item: {shopListMe.getNameCA()}")
        print(f"Amount ordered in pounds: {shopListMe.getAmountCA():.1f}")
        print(f"Price per pound: ${shopListMe.getPriceCA():.2f}")
        print(f"Price of order: ${shopListMe.getcountCA():.2f}")
        
#Caclculate all the item that have been purchased      
def TotalList(yourlist):
    yourtotal = 0
    for i in yourlist:
        yourtotal = i.getcountCA() + yourtotal
    print("Here is your bill dude: ${:.2f}.".format(yourtotal), "Thankyou you and godbless!")

# main function to call all off the function in this driver
def main():
    yourlist = ShopListloop()
    ShowList(yourlist)
    TotalList(yourlist)
    
main()
    


