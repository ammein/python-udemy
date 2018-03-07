"""
Check File directory using python command -> ls

NOTE : Watch out for the line space and indent ! Because it will detect an error on your python. Why ? Because it treated all as an object.

Self NOTE :
Use this in your python terminal for coding style documentation -> print(coding_style.__doc__)

Degression NOTE :
Use this in your python terminal -> degression_link()

Run Python NOTE :
Use default terminal to run python code -> python filename.py

Tuple NOTE :
Use python terminal -> print(what_is_tuple.__doc__)

SETS NOTE :
Use python terminal -> print(what_is_sets.__doc__)

DICTIONARIES NOTE :
use python terminal -> print(what_is_dict.__doc__)

MODULES NOTE :
use python terminal -> print(modules.__doc__)
"""
# IF Statement

#result = int(input("Please enter raw scores : "))
"""
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
"""


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
#while True:
#    pass #busy-wait for keyboard intterupt (Ctrl + C)

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

# For documention degression , open url
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
# Run next(iter_sentence) on terminal over and over again to see iterator on sentence

#LIST
#append
a = [1,2,3]
a.append(4)
#extend (Adding from another list)
b = [1,2,3,4]
b.extend(a)

#insert (Insert on (index , object))
b.insert(3 , 1002)

#remove (if remove cannot find the value , it will return an error)
b.remove(1)

#pop(By default no parameter , it will pop the last in. If value index insert , it will pop on the certain index)
b.pop()

#clear(To remove all item in the list)
b.clear()

#Find index number of '3'
#b.index(3)

#count number for the value
b.count(3)

#sort (Accending Order)
b.sort()

#Sort Reverse
b.sort(reverse=True)

#Reverse (NOT SORT . It just reverse your list)
b.reverse()

#copy
base_eg = [3,4,5,[7. , 5.]]
base_assignment = base_eg
base_assignment[1] = 0.4
base_shallow_copy = base_eg.copy()
base_shallow_copy[1] = 3991 #useful to a]ssign other var with same data but different on each var

#This is to perform deep copy . Use This for import other files or etc
from copy import deepcopy
base_deep_copy = deepcopy(base_eg)
base_deep_copy[1] = 1e44

#To perform copy on certain index
base_deep_copy[3][1] = 2.4e43

# Using lists as a Stack
lifo = list(range(2,6))

lifo.append(3.14)
lifo.pop()

#Using Lists as Queues
#To implement a queue , use collections.deque which was designed to have fast appends and pops from both ends
from collections import deque

name_list = ['John' , 'Michael' , 'Bruce' , 'Abby']
fifo = deque(name_list)

fifo.popleft()

#List Comprehensions
# A concise way to create lists.

#METHOD 1
cubes = []
for n in range(0,10):
    cubes.append(n*n*n)

#METHOD 2
#map = 
cubes = list(map(lambda x: x*x*x, range(10)))

#METHOD 3
cubes = [x*x*x for x in range(0,10)]

#For Loop vs List Comprehension
combs = []
class_1 = ['Jimmy' , 'Audrey' , 'Ono']

for stud_1 in class_1:
    for stud_2 in class_1:
        if stud_1 != stud_2:
            combs.append((stud_1 , stud_2)) #Append multiple arg technique, Use double bracket

x_train = list(range(-4 , 8 , 2)) #from -4 until 8 increment of 2

#Doubling the number
[x**2 for x in x_train]

#Applying absolute to all the elements
[abs(x) for x in x_train]

y_train = ['American Bulldog  ' , 'Berger Picard,' , 'Bullmastiff' , 'Collie' , 'Harrier']

#To remove empty spaces
[y.strip() for y in y_train]

#To remove comma
[y.strip(",") for y in y_train]

#Do Both
[y.strip().strip(",").upper() for y in y_train]

#Unpacked technique from multiple lists
unpacked = []
list_in_list = [['Javanese' , 'Egyptian Mau' , 'Persian'],['Sphynx' , 'Scottish Fold' , 'Manx'],['Korat' , 'Burmese' , 'Bengal']]

for num in list_in_list:
    for n in num:
        unpacked.append(n)

#Shortcut Method
[n for num in list_in_list for n in num]

#Nested List Comprehension
def matrix():
    lala = """
    NOTE :
    Running Row in matrix
    row[i] = 0
    """
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    matrix_expand = [[row[i] for row in matrix] for i in range(4)]
    return {print("Normal Matrix = " , matrix),print("Expand Matrix = " , matrix_expand),print(lala)}

#In the real world , you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case :'
def real_world():
    matrix = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ]
    tuples = print("\t*matrix = ",list(zip(*matrix)))
    wtuples = print("\tmatrix = " ,list(zip(matrix)))
    return tuples , wtuples


#del statement (delete)
cats_list = ['Javanese' , 'Egyptian Mau' , 'Persian' , 'Sphynx' , 'Scottish Fold' , 'Manx']

del cats_list[2]
#to delete all including var
del cats_list


#Tuples and Sequences
#Try below ! Its also tuple ! Shit !
t = 12.54 , 33.33 , 'Blood Moon !'
type(t)

t[0]

#Tuples may be nested
u = t , (1,2,3,4,5)
#Tuples are immutable (Means you cannot change the value of much like string)
#t[0] = 2012

# but they can contain mutable objects:
v = ([2,3,4],[6,7,8])

def what_is_tuple():
    """
    An OUTPUT TUPLES are always enclosed in parentheses, so that nested tuples are interpreted correctly;

    Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
    \t- Tuples are immutable
    \t- Tuples usually contain a heterogenous sequence of elements that are accessed via unpacking or indexing
    \t- Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

    -----------------------------
    \tPROBLEM
    -----------------------------
    CANNOT CONTAIN ONE SINGLE ITEM , IT WILL READ AS FLOAT or STR
    """
    pass

#Empty tuple
empty_t = ()
#if you do only one items/arg , it is NOT a TUPLE
# Try type(failed_single_t)
failed_single_t = ('something')
failed_single_t2 = (12.66)

#But IF comma ADDED
# Try type(single_t)
single_t = (12.66,)

#UNPACKING TECHNIQUE from TUPLE
"""
This is called sequence unpacking and works for any sequence on the right-hand-side.

Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignments is really just a combination of tuple packing and sequnce unpacking.
"""
x , y , z = t




#Sets
def what_is_sets():
    """
    A sets is an unordered collection with NO DUPLICATE ELEMENTS. Basic uses include membership testing and eliminating duplicate entries.
    
    Set objects also support mathematical operations like union, intersection, difference and symmetric difference.

    Curly braces or the set() function can be used to create sets.

    NOTE:
    to create an empty set , you have to use set() , not {} ; the latter creates an empty dictionary,
    """
    pass

shopping_list = ['Macbook' ,'ChromeBook Pixel' , 'Nexus 5X' , 'Nokia N1' , 'Nexus 5X', 'Nexus 5X' ,'Macbook' , 'ChromeBook Pixel']

print("Shopping List = ", shopping_list)
print("Length of Shopping List = " , len(shopping_list))

shopping_list2 = {'Macbook' ,'ChromeBook Pixel' , 'Nexus 5X' , 'Nokia N1' , 'Nexus 5X', 'Nexus 5X' ,'Macbook' , 'ChromeBook Pixel'}

print("SETS Shopping List = ", shopping_list2)
print("SETS Length of Shopping List = " , len(shopping_list2))

#CASE SENSITIVE (Notice the MacBook and Macbook)
'MacBook' in shopping_list
'Macbook' in shopping_list

#Notice duplicate and run this on python
x = set('qweertyyuihsdfop')
y = set('pooiuytrrsdfewqq')

#RUN THIS for SETS
x - y #Letters in x but not in y
x | y #Letters in x or y or both
x & y #letters in both x and y
x ^ y #Letters in x or y but not both


#DICTIONARIES
def what_is_dict():
    """
    Sequences indexed by ranged of numbers,DICTIONARIES are indexed by keys.

    \t- Immutable type,strings and numbers
    \t- Tuples can be used as keys if they contain only strings, numbers, or tuples.
    \t- You can't use lists as keys, since lists can be modified in place using index assignments,slice assignments or methods like append() and extend()

    ----------------------------
    \t REASONS
    ----------------------------
    \t- STORING value with some KEY and extracting the value given by the KEY
    NOTE :
    If using same key , the old key will be forgotten
    ----------------------------
    Reformat KEYS
    ----------------------------
    LIST :
    use -> list(d.keys()) on a dictionary to return a list of all the keys
    SORT :
    use -> sorted(d.keys()) to sorted in arbitary order
    """
    pass
customer_info = {'Jim': 1550 , 'Bob' : 2351}
type(customer_info) # Expected Output : dict

#Adding to DICT
customer_info['Lisa'] = 2351

#Delete DICT
del customer_info['Jim'] #Expected Output : {'Bob' : 2351 , 'Lisa' : 2351}

#Convert to LIST
list(customer_info.keys()) #Expected Output : {'Bob' , 'Lisa' , 'Liz'}

#Test DICT
'Liz' in customer_info #Expected Output : False
'Lisa' in customer_info #Expected Output : True

#dict() constructor builds dictionary directly from sequences of key-value pairs :
dict([('Johnson' , 1008) , ('E1' , 1009) , ('Baye' , 1011)])
#In addition , dict comprehensions can be used to create dictionaries from arbitary key and value expressions
#Notice x with ':' ? That is the KEY
{x:x**3 for x in range(10,16,2)} #x power of 3(x**3)
#When the keys are simple strings , it is sometimes easier to specify pairs using keyword args. (MOST RECOMMENDED)
dict(Johnson = 1008 , E1 = 1009 , Baye = 1011)

#Looping Techniques
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

scale = {'small' : 'S' , 'large' : 'L'}

for key ,value in scale.items():
    print(key , value)

"""
EXPECTED OUTPUT :
small S
large L
"""

# To loop over two or more sequences at the same time , the entries can be paired with the zip() function
AAPL = [172.5 , 170.1 , 160.5]
IBM = [80.5 , 83.52 , 84.53]

for stk1 , stk2 in zip(AAPL , IBM):
    print('AAPL={0} IBM={1}'.format(stk1 , stk2))

"""
EXPECTED OUTPUT :
AAPL = 172.5 IBM=80.5
AAPL = 170.1 IBM=83.52
AAPL = 160.5 IBM=84.53
"""

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered
basket = ['apple' , 'orange', 'apple' , 'pear' , 'orange' , 'banana']\


for f in sorted(set(basket)):
    print(f)
"""
EXPECTED OUTPUT :
apple
banana
orange
pear
"""

#it is sometimes tempting to change a list while you are looping over it; however, it is often simple and safer to create a new list instead
# Run -> filtered_data
import math
raw_data = [56.2 , float('NaN'), 51.7 , 55.3 , 52.5 , float('Nan') , 47.8]

filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

def modules():
    """
    Have you ever realized that you have to run the code over and over again ?

    The functions and var are lost ? If you want to write a somewhat LONGER PROGRAM , you are better off using a text editor to prepare the input for the interpreter and runnint it with that files as input instead. 

    This is known as creating SCRIPT.

    Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a 'module'; definitions from a module can be imported into other modules or into 'main' module(the collection of variables that you have access to in a script executed at the top level and in calculator mode)

    A module is a file containing Python definitions and statements. The file name is the module name with the suffix '.py' appended. Within a module, the module's name (as a string) is available as the value of the global variable __name__. For instance, use your favourite text editor to create a file called fibo.py in the current directory

    NOTE :
    You may want to split it into several files for easier maintenance.

    You may want to use a handy function that you've written in several programs without copying its definition into each program.
    """
    pass


print(50 * "*" , "\nLOAD SUCCESSFUL\n" , 50 * "*")


if __name__ == "__main__":
    import sys
    long_list(int(sys.argv[1]))