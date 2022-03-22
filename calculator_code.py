#Hi all welcome to my first program This is a basic calculator that will repeat for you
#Any feedback contact me @ truegarythompson@gmail.com Thank you! Enjoy!
print ("Hi welcome to the Gary Calculator")

print ("First what is your name?")

name = input()

print("Hi",name,"!","Let's Do This!")

#This is the code to run the program for math equations
while True:

    x   = int(input("Put your first number: "))

    y = int(input("Put your second number: "))

    print ("With Multiplication your answer is", x , "*", y,"=", x*y)

    print ("With Addition your answer is", x , "+", y,"=", x+y)

    print ("With Subtraction your answer is", x , "-", y,"=", x-y)

    print ("With Division your answer is", x , "/", y,"=", x/y)

    print ("do you want to play again?")

    repeat = input("Type Y or N: ")

    if(repeat == ("Y")) :
        print ("Okay lets go again!")
    else : 
        print ("Okay bye!")
        exit()
        
