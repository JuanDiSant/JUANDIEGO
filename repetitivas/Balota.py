ValorCompra=0
Descuento=0
Balota=0
ValorCompra=int (input ("digite el valor de la variable valor_compra: "))
ColorBalota=input("ingrese el color de la balota: ")

if ValorCompra>=50000 and ColorBalota=="roja":
    descuento=ValorCompra-(ValorCompra*0.1)
    print(f"sacaste la balota roja, el valor de la compra es {ValorCompra} y el total a pagar: {descuento}")
elif ValorCompra>50000 and ColorBalota=="verde":
    descuento=ValorCompra-(ValorCompra*0.015)
    print(f"sacaste la balota verde, el valor de la compra es {ValorCompra} y el total a pagar: {descuento}")
elif ValorCompra>50000 and ColorBalota=="azul":
    descuento=ValorCompra-(ValorCompra*0.2)
    print(f"sacaste la balota azul, el balor de la compra es {ValorCompra} y el total a pagar: {descuento}")
elif ValorCompra>50000 and ColorBalota=="amarilla":
    descuento=ValorCompra-(ValorCompra*0.5)
    print(f"sacaste la balota amarilla el valor de la compra es {ValorCompra} y el total a pagar: {descuento}")
    
elif ValorCompra>50000 and ColorBalota=="negra":
    descuento=ValorCompra-(ValorCompra)
    print(f"sacaste la balota negra el valor de la compra es {ValorCompra} y el total a pagar: {descuento}")
    
elif ValorCompra<50000:
    print(f"no participas en el sorteo y en total a pagas: {ValorCompra}")