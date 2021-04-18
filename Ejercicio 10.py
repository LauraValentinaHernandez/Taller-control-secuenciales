"""
entrada
chilines-->float-->chi
dracmas-->float-->drac 
pesetas-->float-->pese 
salidas
peseta-->float-->pes
frascos-->float-->franc
dolar-->float-->dolar
liras-->float-->lira
salida
"""
#entrada
chi=float(input("Digite monto en Chilines: "))
drac=float(input("Digite monto en Dracmas: "))
pese=float(input("Digite monto en Pesetas: "))
#cajanegra
pesetas=((chi*956871)/100)
francos=(((drac*88607)/100)*(1/20110))
dolares=(pese/122499)
liras=((pese*100)/9289)
#salidas
paint("La cantidad de chelines a pesetas es: ")+str(pesetas),"La cantidad de dracmas a francos franceses es: "+str(francos),"La cantidad de pesetas a dolares es: "+str(dolares), "La cantidad de pesetas a liras es: "+str(liras))