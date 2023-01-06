numero = int(input('Digite um número para ver a tabuada: '))
print('{:=^20}'.format(''))

    
for cont in range (1,11):
    print('{} x {} = {}'.format(numero, cont, numero*cont))