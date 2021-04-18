"""
entrada
compra-->float-->compra
salida
descuento-->float-->desc
total-->float-->total
"""
#entrada
compra=int(input("Digite valor total de la compra:"))
#cajanegra
desc=compra*0.15
total=compra-desc
#salida
print("Pago total con % "+str(total))