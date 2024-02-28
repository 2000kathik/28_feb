from hello import hello
def test_default():
    assert hello()=="hello,wings"
def test_argument():
    assert hello("wings")=="hello, infonet"