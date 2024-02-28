# Import the square function from the squar module
from squar import square
#This function is responsible for testing the square function
def test_square():
#assert statement is used for debugging purposes and to perform assertions in your code
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0

# Test case for square function with a string input
def test_str():
# Use pytest.raises context manager to check for a TypeError
    with pytest.raises(TypeError):
        square("cat")
