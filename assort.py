# Import the square function from the squar module
from squar import square
# This is the main function where the program execution begins
def main():
#Calls the test_square function when the program runs.
    test_square()
def test_square():
# Use assert statements to check if square(2) equals 4
    assert square(2)==4
# Use assert statements to check if square(3) equals 9
    assert square(3)==9
if __name__=="__main__":
    main()