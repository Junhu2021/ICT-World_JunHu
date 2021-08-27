##1.	Create a program that fulfils the following requirements:
##
##a)	Asks for the user’s last name.
##
##b)	Presents a list of toppings and asks the user to select toppings until the user selects the “Done” option.
##•	Cheese
##•	Pineapple
##•	Pepperoni
##•	Ham
##•	Everything
##•	Done (Finished selecting toppings)
##
##c)	Calculate the price based on the number of toppings
##•	One topping = $8
##•	Two toppings = $10
##•	Three toppings = $12
##•	Four toppings or Everything = $14
##
##d)	Prints to the screen the user’s last name, a listing of the toppings they chose, and the total price.
##
##e)	Remember to comment your code:
##•	Name of programmer
##•	Date program written
##•	Short description of purpose of program

## Ask the user's last name
lastName = input('Please input your last name : \n')
## define a funtion to return different types of toppings for the user to select
def items(key):
    if (key == 1):
        return "Cheese"
    elif (key == 2):
        return "Pineapple"
    elif (key == 3):
        return "Pepperoni"
    elif (key == 4):
        return "Ham"
    elif (key == 5):
        return "poop"
    else:
        return "Done(Finished selecting toppings)"
## create a key list for 6 options
keys = [1,2,3,4,5,6]
## create a dictionary for the prices based on the number of toppings
price = {1:8,2:10, 3:12,4:14}
## Create an empty topping list to put the user choosing
toppingList=[]
##create a list to put the option number of the chosen topping 
numberTopping = []
## create a varaible for the total payment
tally = 0
## creat a variable to put the number of topping the user chooses
toppingNumber = 0
choosing = True
## Use while loops to print the topping types 
while (choosing):
    for i in range(0, len(keys)):
        x = keys[i]
        print(str(x) + ".) " + items(x))
    choice = input('choose a topping:\n')
## the user selects the “Done” option to exit. Also the program would exit if an invalid number is input
    if (int(choice) == 6):
        choosing = False
    elif (int(choice) >6) or (int(choice) < 1):
       choosing = False
       print (' you input an invalid number')
       exit()
## calculate the total charge for four toppings or Everything = $14
    elif(toppingNumber == 4) or (int(choice) == 5):
        choosing = False
        tally =  price [4]
        toppingList.append(items(5))
## use choose 1-3 topping and locate their relevant price
    else:
        toppingNumber = toppingNumber+1
        tally = price[toppingNumber]
        toppingList.append(items(int(choice)))
## remove the slected toppings
    keys.remove(int(choice))
    numberTopping.append(int(choice))
print("Hello, "+ lastName+ ". you chose :" )
##print a listing of the topping they chose with choosing options sorted by choosing sequence
for i in range(0, len(toppingList)):
    print(str(numberTopping[i])+ ".) "+ toppingList[i])
print("Your total comes to: ${:.2f}".format(tally,2))
## program name: Jun Hu
## Date program written : August 21,2021
## descrition of purpose of program: generate a pizza toppings order for customers and let them choose and calculated the total charge by printing the receipt
