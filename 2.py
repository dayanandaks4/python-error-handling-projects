def Calcultor():
    print("welcome to calculator:")
    print("additon  =>1")
    print("sub   =>2")
    print("mul   =>3")
    print("div  ==>4")
    print("power ==>5")
    print("exit ===> 6")
    print("<=========================>")



    avilable_data = [1,2,3,4,5,6]
    while True:
        try:
            opertion = int((input("enter the opertion:")).strip())
        except ValueError:
            print("Enter only one number,excpet number dont enter anything")
            continue
        if opertion in avilable_data:  
            if opertion == 6:
                print("Thank you")
                break
            else: 
                while True:
                    try:
                        num1 = float((input("enter the first number:")).strip())
                        break
                    except ValueError:
                        print("Enter number only, not anything excpet number")
                while True:
                    try:
                        num2 = float((input("enter the second number:")).strip())
                        break
                    except ValueError:
                        print("enter valid")
                
                if opertion == 1:
                    sum = num1+num2
                    print("Sum of two number:",sum)
                elif opertion == 2:
                    sub = num1-num2
                    print("Sub of two number:",sub)        
                elif opertion == 3:
                    mul = num1*num2
                    print("mul of two number:",mul)
                elif opertion == 4:
                    if num2 == 0:
                        print("its not Divisbale")
                    else:
                        div = num1/num2
                        print("div of two number:",div)
                elif opertion == 5:
                    power = num1**num2
                    print("power of two number:",power)
        else:
            print("Enter valid opertion (1 to 6)")


Calcultor()
Calcultor()