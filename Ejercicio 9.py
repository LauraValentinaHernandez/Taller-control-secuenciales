"""
entrada
sueldobase-->float-->s
horas-->int-->h
salida
valorhora-->float-->valorh
salariohora-->float-->salarioh
descuimp-->float-->desc
pago-->float-->pag 
"""
#entrada
s=float(input("Digite sueldo base del empleado: "))
h=float(input("Digite horas que trabajo el empleado en el mes: "))
#cajanegra
valorh=s/h
salarioh=valorh*h
desc=s*0.20
pag=salarioh-desc
#salida
print("Pago salario neto:"+str(pag))
