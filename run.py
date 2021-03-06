# check index doc
import index
while True:
    try:
        inp = int(input("Enter 1 (import degression_link and modules function only) Enter 2 (import ALL function) : \n"))
        if inp == 1:
            #More on Modules
            #less practical code
            from index import degression_link , modules
            print(200 * "-")
            print(degression_link.__doc__)
            print(modules.__doc__)
            break
        elif inp == 2:
            #NOW this is COOL ! IMPORT EVERYTHING and GLOBAL THEM
            from index import *
            #degression_link()
            print(200 * "-")
            print(index.__doc__)
            break #Break means , execute ONCE !
    except ValueError:
        print(100 * "*" , sep='\n')
        print("WRONG INPUT ! Please choose number between 1 or 2 and Try again.")
        print(100 * "*" ,sep='\n')
    finally:
        print("Successful Loaded the file !")


#Executing modules as scripts
def execute():
    """
    Run python module with :
    python index.py <arguments>

    Adding the code at the end of your module :
    if __name__ == "__main__":
        import sys
        index(int(sys.argv[1]))
    """
    pass


#Standard Modules
def standard_module():
    """
    Run this on python terminal to list out all var and def function:
    dir(filename) -> all that defined in the file location
    dir() -> all that defined currently
    """
    pass


def packages():
    """
    Suppose you want to design a collection of modules(a "package") for the uniform handling of sound files and sound data. There are many different sound file formats(usually recognized by their extension .wav .aiff .au) , so you may need to create and maintain a growing collection of modules for the conversion between the various formats. There are also many different operations you might want to perform on sound data (such as mixing , adding echo , applying an equalizer function , creating an artificial stereo effect).

    So in addition , you will be writing a never-ending stream of modules to perform these operations. Here's a possible structure for your package (expressed in terms of a hierarchical filesystem):
    
    Example :
    sound/
        __init__.py
        formats/
            __init.py
            waveread.py
            aiffread.py
            auread.py
            auwrite.py
            ...
        effects/
            __init__.py
            echo.py
            surround.py
            reverse.py
            ...
        filters/
            __init__.py
            equalizer.py
            vocoder.py
            karaoke.py
            ...


    The __init__.py files are REQUIRED to make Python treat the directories as containing packages; This is done to prevent directories with a common name such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it also execute initialization code for the package or set the __all__ variable.

    Users of the package can import individual modules from the package, for example :
    import sound.effects.echo

    This loads the submodule sound.effects.echo. It must be referenced with its full name :
    sound.effects.echo.echofilter(input , output , delay = 0.7 , atten = 4)

    An alternative way of importing the submodule is :
    from sound.effects import echo

    This loads the submodule echo , and makes it available without its package prefix, so it can be used as follows :
    echo.echofilter(input , output , delay = 0.7 , atten = 4 )
    """
    pass

#Importing * from a package
def package_all():
    """
    What happens when you try to import 'from sound.effects import *' ? 

    The import statement uses the following convention: if a package's __init__.py code defines a list named __all__ , it is taken to be the list of module names that should be imported when 'from package import *' is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don't see a use for importing * from their package. For example , the file sound/effects/__init__.py could contain the following code :

    __all__ = ["echo" , "surround" , "reverse"]

    This would mean that 'from sound.effects import * would import the three named submodules of the sound package.
    """
    pass
