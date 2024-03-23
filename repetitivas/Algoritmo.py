ValorCompra = int(input("Digite el valor para la variable valor_compra: "))
Descuento = 0.05
ValorTotal = ValorCompra-(ValorCompra*Descuento)
print("el valor de la compra es de ",ValorTotal)



#segundo
x= int(input("Digite el valor para la variable x: "))



if x > 5:
    print("x es mayor que 5")
else: print("x no es mayor que 5)")

#Segundo algoritmo
Descuento = 0

if ValorCompra  > 50000:
    Descuento = ValorCompra * 0.10
elif ValorCompra==0:
    print("No genera desceunto ")    
elif ValorCompra < 50000:
    Descuento = ValorCompra * 0.05
elif ValorCompra == 50000:
    Descuento = ValorCompra * 0.07


