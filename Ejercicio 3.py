"""
Entradas
venta1-->float-->v1
venta2-->float-->v2
venta3-->float-->v3
sueldobase-->float-->sb
Salidas
comision-->float-->c
total-->float-->total
"""
#entradas
v1=float(input("Digite la venta 1:"))
v2=float(input("Digite la venta 2:"))
v3=float(input("Digite la venta 3:"))
sb=float(input("Digite suelde base:"))
#caja negra
comision=(v1+v2+v3)*0.10
total=sb+comision
#salidas
print("Comision es:"+str(comision),"Sueldo total:"+str(total)) 
