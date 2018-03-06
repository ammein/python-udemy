import index
# check index doc

inp = int(input("Enter 1 (import degression_link and modules function only) Enter 2 (import ALL function) : \n"))

if inp == 1:
    #More on Modules
    #less practical code
    from index import degression_link , modules
    print(degression_link.__doc__)
    print(modules.__doc__)
    #degression_link() #it will become global ! COOL but LESS PRACTICAL
elif inp == 2:
    #NOW this is COOL ! IMPORT EVERYTHING and GLOBAL THEM
    from index import *
    #degression_link()
    print(index.__doc__)
else:
    print("WRONG INPUT !")
    pass
