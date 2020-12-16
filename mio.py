print("ciao")
print("/// SOMMA DI UNA LISTA ///")
listaz = [4,5,4,5,4,5,4,5]
def sommaLista (lista):
    sum=0
    for item in lista:
        sum = item + sum
    print ("somma: {}".format(sum))
sommaLista(listaz)


print("/// SOMMA LISTA CON RETURN ///")
def sommaReturn (list):
    sum = 0
    for item in list:
        sum = sum + item
    return sum

print("la somma è: {}".format(sommaReturn(listaz)))