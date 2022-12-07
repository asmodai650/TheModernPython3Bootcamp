#age = input("How old are you: ")
#if age:
#    age = int(age)
#    if age >= 18 and age < 21:
#        print("You can enter, but need a wristband.")
#   elif age >= 21:
#        print("You can enter and drink.")
#    else:
#        print("You cant enter!")
#else:
#    print("Please enter an age using numbers only!")



#### REFACTORED ####
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink.")
    if age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You cant enter!")
else:
    print("Please enter an age using numbers only!")
