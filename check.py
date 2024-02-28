# Import the square function from the squar module
from squar import square
# This is the main function where the program execution begins
def main():
#Calls the test_square function when the program runs.
    test_square()
#This function is responsible for testing the square function
def test_square():
#Checks if the square of 2 is not equal to 4.
# If true, it prints a message indicating that the square of 2 was not 4.
    if square(2)!=4:
        print("2 was not 4")
    if square(3)!=9:
        print("3 square was not 9")
#block ensures that the code is executed only when the script is run directly.
if __name__=="__main__":
    main()