# Import the square function from the squar module
from squar import square
# This is the main function where the program execution begins
def main():
    test_square()
def test_square():
# Use try-except blocks to handle assertions and print custom messages on failure
    try:
        assert square(2)==4
    except AssertionError:
        print("2 square is not 4")
# Use try-except blocks to handle assertions and print custom messages on failure
    try:
        assert square(3)==9
    except AssertionError:
        print("2 square is not 9")
if __name__=="__main__":
    main()