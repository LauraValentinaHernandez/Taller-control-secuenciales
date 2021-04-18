"""
entrada
mujeres-->int-->muj
hombre-->int-->hom
salida
mujer-->int-->mujer
hombre-->int-->hombre
"""
#entrada
muj=int(input("Digite numero total de mujeres: "))
hom=int(input("Digite numero total de hombres: "))
#cajanegra
est=muj+hom
mujer=((muj*100)/est)
hombre=((hom*100)/est)
#salidas
print("Porcentaje mujeres: "+str(mujer),"Porcentaje hombres: "+str(hombre))
