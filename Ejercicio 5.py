"""
entradas
parcial1-->float-->p1
parcial2-->float-->p2
parcial3-->float-->p3
examenf-->float--exf
trabajof-->float-->trf
salidas
promedioparcial-->float-->promedio
efinal-->float-->exfinal
tfinal-->float-->trfinal
notafinal-->float-->notafinal
"""
#entrada
p1=float(input("Digite nota calificacion parcial 1: "))
p2=float(input("Digite nota calificacion parcial 2: "))
p3=float(input("Digite nota calificacion parcial 3: "))
exf=float(input("Digite nota examen final: "))
trf=float(input("Digite nota trabajo final: "))
#cajanegra
promedio=((p1+p2+p3)/3)*0.55
exfinal=exf*0.30
trfinal=trf*0.15
notafinal=promedio+exfinal+trfinal
print("Nota final es:"+str(notafinal))
