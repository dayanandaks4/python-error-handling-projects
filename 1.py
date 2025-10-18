# Simple calculator using Python
def Calculator_display():
    print("Welcome TO Our Calculator")
    print("Addition       -----------------> 1")
    print("Subtraction    -----------------> 2")
    print("Multiplication -----------------> 3")
    print("Division       -----------------> 4")
    print("Power          -----------------> 5")
    print("Stop          -----------------> 6")
Calculator_display()
def add():
    sum = user_1+user_2
    print("Sum of two number is ",sum)
add()
    
opertion = int(input("Enter the opertion (1 to 6):"))
if opertion == 6:
    print("Thank you")
else:
    user_1 = int(input("Enter the First Number:"))
    user_2= int(input("Enter the Second Number:"))

    if opertion == 1 :
        print(add())
    if opertion == 2:
        print(sub())
    if opertion == 3:
        print(mul())
    if opertion == 4:
        print(div())
    else:
        print(power())


    
    
        



