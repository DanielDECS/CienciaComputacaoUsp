def maximo(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def test_maximo0():
    assert maximo(1,2) == 2

def test_maximo1():
    assert maximo(3,2) == 3

def test_maximo2():
    assert maximo(5,9) == 9
