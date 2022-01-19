def Option1():
    print("Congratulations, you have chosen Option One, the best option!")
def Option2():
    print("You have chosen Option Two, the not the best option...")
def Option3():
    print("Oh no, you have chosen Option Three, the most terrible option")

def Menu():
    answer = input("Pick either Option 1, Option 2, or Option3 please")
    if answer == "Option1":
        Option1()
        Menu()
    elif answer == "Option2":
        Option2()
        Menu()
    elif answer == "Option3":
        Option3()
        Menu()
    else:
        print("You failed and have no more chances to succeed...")
Menu()
