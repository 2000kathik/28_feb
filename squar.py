# This is the main function where the program execution begins
def main():
    x=int(input("the given value of x :"))
#The square() function is defined with a docstring that explains its purpose, arguments (x) and return value.
    print("x square is ",square(x))
# Function to calculate the square of a number
def square(x):
#return the x+x vlaue to the square(x)
    return x+x
#block ensures that the code is executed only when the script is run directly.
if __name__=="__main__":
# If this code is run as the main program, execute the main function.
    main()