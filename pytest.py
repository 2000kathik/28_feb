# Import the square function from the squar module
from squar import square
# Test positive numbers
def test_pos():
    #assert statement is used for debugging purposes and to perform assertions in your code
    assert square(2)==4
    assert square(3)==9
# Test negative numbers
def test_netve():
    #assert statement is used for debugging purposes and to perform assertions in your code
    assert square(-2)==4
    assert square(-3)==9
# Test zero
def test_zero():
    #assert statement is used for debugging purposes and to perform assertions in your code
    assert square(0)==0