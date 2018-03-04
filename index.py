"""
NOTE : Watch out for the line space and indent ! Because it will detect an error on your python. Why ? Because it treated all as an object.

Self NOTE :
Use this in your python terminal for coding style documentation -> print(coding_style.__doc__)

Degression NOTE :
Use this in your python terminal -> degression_link()

Run Python NOTE :
Use default terminal to run python code -> python filename.py
"""
# IF Statement

result = int(input("Please enter raw scores : "))

if result >= 91:
    print("A+")
elif result >= 75:
    print("A")
elif result >= 60:
    print("B")
elif result >= 50:
    print("C")
elif result >= 35:
    print("D")
elif result >= 20:
    print("E")
else:
    print("U")



# For Loops begin

fruit_collection = ['apple' , 'orange' , 'guava' , 'durian' , 'rambutan']

for f in fruit_collection:
    print(f , len(f) , f.upper())

for i in range(5):
    print(i)

for i in range(-4 , 4 , 2):
    print(i)

for i in range(len(fruit_collection)):
    print(i , fruit_collection[i])

# enumerate allows us to loop over iterable items(for loop) and generates an automatic counter. shorten code from above

for k , v in enumerate(fruit_collection):
    print(k , v)

range(4)

list(range(4))

for f in fruit_collection:
    if f == "durian":
        print("Found the smelly fruit !!! -->",f)
        break
    else:
        print("Love this fruit" , f)

#continue means else

for n in range(2,10):
    if n % 3 == 0:
        print("Found a number divisible by 3 -->" , n)
        continue #inform the loop to continue with the next item (Try to comment continue and see what happens)
    print("Just another number" , n)


# pass statements
while True:
    pass #busy-wait for keyboard intterupt (Ctrl + C)

# function
def calculate_random(object):
    pass

# Defining Function
def square_fn(obj):
    """
    this is the doc string
    
    This function squares the input

    Parameters
    ------------
    obj : float
        Input Number.

    Returns
    -------------
    square float
        Squared number
    """
    return obj * obj

def fib2(n):
    result = []
    a , b = 0 , 1
    while a < n:
        result.append(a)
        a,b = b , a + b
    return result

f100 = fib2(100) # You also can assign to var

f100.append(100) # Powerful function if you assign var . More built-in function will be display

def car_color(color = 'red'):
    print(color)

car_color(color = 'blue')

my_color = 'green'

def water_color(arg = my_color):
    print(arg)

#Multiple numbers
"""
def fl(a , L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
"""
# Standalone numbers by themself
def fl(a , L = None):
    if L is None:
        L = []
    L.append(a)
    return L

#Can define one type of argument needed (a). The rest are default
def parrot(a , b ='plant' , c = 'cat' , d = 'red'):
    print("The first argument is", a)
    print("Animal Versus" , b)
    print("Computer vision comparing dogs versus" , c)
    print("The sky is" , d)

#Take this note ! Useful tuple for function
#Try to key in function this : long_list("fruits" , "banana" , "mango" , Australia = "Orange" , US = "Sunkist")
"""
                        NOTE :
When a final parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name)
"""
def long_list(fruit, *tropic , **temperate):
    print("\n\n\t\t"+fruit)
    print(50 * "*")
    print("\t[INFO] This is in *tropic")
    for t in tropic:
        print(t)
    print(50 * "*")
    print("\t[INFO] This is in **temperate")
    for kw in temperate:
        print(kw , ":" , temperate[kw])
    print(50 * "*")
    print("\n\n")


list(range(3,6))

args = [3 , 6]
list(range(*args)) #tuple happens (Priority)

# lambda is like function but compact (Just like if else javascript shortcut)
sqrt = lambda m , n: m * (1/n)
sqrt(4,2)

def sqrt_func(m , n):
    return m ** (1/n)
# Do this in terminal for result : sqrt_func(4,2)

#Doc Strings

def my_func():
    """
    This is just a doc string for function definitions
    """
    pass

#type this in terminal to present output on function : print(function_name.__doc__)

def coding_style():
    """
    - Use 4-space indentation , and no tabs
    - 4 spaces are good compromise between small indentation (allows greater nesting depth) and large indentation(easier to read). Tabs introduce confusion, and are best left out.
    - Wrap lines so that they don't exceed 79 characters.
    - This helps users with small displays and makes it possible to have several codes files side-by-side on larger displays.
    - Use blank lines to separate functions and classes , and larger blocks of code inside funtions.
    - When possible , put comments on a line of their own
    - Use docstrings !
    - Use spaces around operators and after commas , but not directly inside bracketing constructs : a = f(1, 2) + g(3, 4)
    - Name your classes and functions consistently ; the convention is to use 'Camelcase' for classes and 'lower_case_with_underscores for functions and methods.
    - Don't use fancy encodings if your code is meant to be used in international environments. Python's default, UTF-8, or even plain ASCII work best in any case.
    - Likewise , don't use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.
    """
    pass

# For documention , open url
import webbrowser
url = 'https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols'
def degression_link():
    """
    if new is 0, will open on same browser. If 1 , new browser. if 2 , new browser page tab on opened browser
    """
    return webbrowser.open(url , new = 2 , autoraise=True)

# Iterable , Iterator and next() & __iter__() method
"""
an ITERABLE
a str object that is immutable
no state
has a __getitem__() method
"""
sentence = 'classic text'
"""
an ITERATOR
has state (it starts by pointing at the "c" in "classic text")
has a next() method and an __iter__() method
"""
iter_sentence = iter(sentence)