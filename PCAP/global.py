def myFunction():
    global var
    var = 2
    print("Valor: ", var)
var = 1
myFunction()
print(var)