def ePrimo(x):
    primo = True
    fator = 2
    while fator < x and primo:
        if x % fator == 0:
            primo = False
        fator = fator + 1
        
    if primo and x != 1:
        return True
    else:
        return False

def maior_primo(n):
    c = 2
    while c <= n:
        if ePrimo(n) == True:
            return n
        else:
            n = n - 1
