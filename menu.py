def printblue():
    print("You chose blue!\r\n")
def printred():
    print("You chose red!\r\n")
def printorange():
    print("You chose orange!\r\n")
def printyellow():
    print("You chose yellow!\r\n")


colorselect = {
    0 : printblue,
    1 : printred,
    2 : printorange,
    3 : printyellow
}

selection = 0
while selection != 4:
    print("0. Blue")
    print("1. Red")
    print("2. Orange")
    print("3. Yellow")
    print("4. Quit")
    selection = int(input("Select a color option: "))
    if selection >= 0 and selection < 4:
        colorselect[selection]()
