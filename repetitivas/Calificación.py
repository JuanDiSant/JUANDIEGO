Calificacion1 = int(input("ingrese la calificacion del estudiante 1:"))
Calificacion2 = int(input("ingrese la calificacion del estudiante 2:"))
Calificacion3 = int(input("ingrese la calificacion del estudiante 3:"))
Calificacion4 = int(input("ingrese la calificacion del estudiante 4:"))
Calificacion5 = int(input("ingrese la calificacion del estudiante 5:"))
Calificacion6 = int(input("ingrese la calificacion del estudiante 6:"))
Calificacion7 = int(input("ingrese la calificacion del estudiante 7:"))
Calificacion8 = int(input("ingrese la calificacion del estudiante 8:"))
Calificacion9 = int(input("ingrese la calificacion del estudiante 9:"))
Calificacion10 = int(input("ingrese la calificacion del estudiante 10:"))

menor_50=0
entre_50_y_70=0
entre_70_y_80=0
mayor_80=0

if Calificacion1>=1 and Calificacion1<=49:
    menor_50 +=1
elif Calificacion1>=50 and Calificacion1<=69:
    entre_50_y_70 +=1
elif Calificacion1 >= 70 and Calificacion1 < 79:
    entre_70_y_80 += 1
elif Calificacion1>=80 and Calificacion1<=100:
    mayor_80 +=1

if Calificacion2>=1 and Calificacion2<=49:
    menor_50 +=1
elif Calificacion2>=50 and Calificacion2<=69:
    entre_50_y_70 +=1
elif Calificacion2 >= 70 and Calificacion2 < 79:
    entre_70_y_80 += 1
elif Calificacion2>=80 and Calificacion2<=100:
    mayor_80 +=1

if Calificacion3>=1 and Calificacion3<=49:
    menor_50 +=1
elif Calificacion3>=50 and Calificacion3<=69:
    entre_50_y_70 +=1
elif Calificacion3 >= 70 and Calificacion3 < 79:
    entre_70_y_80 += 1
elif Calificacion3>=80 and Calificacion3<=100:
    mayor_80 +=1

if Calificacion4>=1 and Calificacion4<=49:
    menor_50 +=1
elif Calificacion4>=50 and Calificacion4<=69:
    entre_50_y_70 +=1
elif Calificacion4 >= 70 and Calificacion4 < 79:
    entre_70_y_80 += 1
elif Calificacion4>=80 and Calificacion4<=100:
    mayor_80 +=1

if Calificacion5>=1 and Calificacion5<=49:
    menor_50 +=1
elif Calificacion5>=50 and Calificacion5<=69:
    entre_50_y_70 +=1
elif Calificacion5 >= 70 and Calificacion5 < 79:
    entre_70_y_80 += 1
elif Calificacion5>=80 and Calificacion5<=100:
    mayor_80 +=1

if Calificacion6>=1 and Calificacion6<=49:
    menor_50 +=1
elif Calificacion6>=50 and Calificacion6<=69:
    entre_50_y_70 +=1
elif Calificacion6 >= 70 and Calificacion6 < 79:
    entre_70_y_80 += 1
elif Calificacion6>=80 and Calificacion6<=100:
    mayor_80 +=1

if Calificacion7>=1 and Calificacion7<=49:
    menor_50 +=1
elif Calificacion7>=50 and Calificacion7<=69:
    entre_50_y_70 +=1
elif Calificacion7 >= 70 and Calificacion7 < 79:
    entre_70_y_80 += 1
elif Calificacion7>=80 and Calificacion7<=100:
    mayor_80 +=1

if Calificacion8>=1 and Calificacion8<=49:
    menor_50 +=1
elif Calificacion8>=50 and Calificacion8<=69:
    entre_50_y_70 +=1
elif Calificacion8 >= 70 and Calificacion8 < 79:
    entre_70_y_80 += 1
elif Calificacion8>=80 and Calificacion8<=100:
    mayor_80 +=1

if Calificacion9>=1 and Calificacion9<=49:
    menor_50 +=1
elif Calificacion9>=50 and Calificacion9<=69:
    entre_50_y_70 +=1
elif Calificacion9 >= 70 and Calificacion9 < 79:
    entre_70_y_80 += 1
elif Calificacion9>=80 and Calificacion9<=100:
    mayor_80 +=1

if Calificacion10>=1 and Calificacion10<=49:
    menor_50 +=1
elif Calificacion10>=50 and Calificacion10<=69:
    entre_50_y_70 +=1
elif Calificacion10 >= 70 and Calificacion10 < 79:
    entre_70_y_80 += 1
elif Calificacion10>=80 and Calificacion10<=100:
    mayor_80 +=1
    
print("la cantidad de estudiantes que obtuvieron calificacion menor a 50 es:", menor_50)
print("la cantidad de estudiantes que obtuvieron calificacion entre 50 y 69 es:", entre_50_y_70)
print("la cantidad de estudiantes que obtuvieron calificacion entre 70 y 79 es:", entre_70_y_80)
print("la cantidad de estudiantes que obtuvieron calificacion mayor a 80 es:", mayor_80)
