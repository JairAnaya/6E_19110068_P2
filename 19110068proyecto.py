"""
Jair Shiblón Anaya Rodríguez
19110068
6E6
Sistemas Expertos
Proyecto
"""
import cv2
import os

cont = 0 #Contador para puntaje de sección de morfología
cont2 = 0 #Contador para puntaje de sección de repetición de palabras

print("Tamiz de problemas del lenguaje - TPL") 
print("Se utiliza para identificar trastornos o retrasos expresivos o bien, receptivo-expresivos del lenguaje")
print("La prueba TPL está dividida en dos secciones. La primera trata sore la tarea de morfología y la segunda sobre repetición de oraciones.")
print("La prueba se realiza a niños mexicanos monolingües en los siguientes rangos de edad:")
print("3 años - 3 años con 5 meses")
print("3 años con 6 meses - 3 años con 11 meses")
print("4 años - 4 años con 5 meses")
print("4 años con 6 meses - 4 años con 11 meses")
print("5 años - 5 años con 11 meses")
print("6 años - 6 años con 11 meses")
print("Al escribir la edad se escribirá de la siguiente manera: por ejemplo, si el niño tiene 3 años con 5 meses, se escribirá 3 en la parte de edad y 5 en la parte de meses, si tiene 6 años con 11 meses, se escribirá 6 en la parte de edad y 11 en la parte de meses")

os.system('pause')
os.system('cls')

#Se obtiene la información del niño, en especial la información de la edad para que se evalúe en su rango
nombre = input("Nombre: ")
edad = input("Edad: ")
meses = input("Meses: ")
edadRango = int(edad)
mesesRango = int(meses)
print("Fecha: ")
dia = input("Día (dos dígitos): ")
mes = input("Mes (dos dígitos): ")
anho = input("Año (cuatro dígitos): ")
fecha = [dia, mes, anho]
lugar = input("Lugar: ")

os.system('cls')

#print(nombre, edad, "(", dia, "/", mes, "/", anho, ")", lugar)

print("Morfología")
print("En esta primera sección se evaluará la parte morfológica del lenguaje. La tarea de morfología contiene 13 reactivos (preguntas de respuesta cerrada) divididos en cuatro secciones.")
print("Éstas contienen los 4 tipos de partículas morfológicas que resultan ser las más vulnerables en español: artículos, clíticos, preposiciones y palabras reservadas.")
os.system('pause')

print("Sección A: Artículos")

print("Ejemplo: ")
print("Vamos a ver unos dibujos y tú me dices qué son. Mira, ¿qué hay aquí? (Hay que esperar la respuesta del niño, si no la dice entonces se da la respuesta).")
print("\u0332".join("UNA"), "abeja /", "\u0332".join("UN"), "bicho")
os.system('pause')
imagen1 = cv2.imread('1.png')
cv2.imshow('Logo OpenCV',imagen1)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system("PAUSE")

print("1. ¿A quiénes les lee la gallina?")
print("A", "\u0332".join("LOS"), "/", "\u0332".join("UNOS"), "ratones")
os.system('pause')
imagen2 = cv2.imread('2.png')
cv2.imshow('Logo OpenCV',imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp1 = input("Escriba la respuesta del niño (LOS, UNOS): ")

print("2. ¿Cuáles animales hacen siempre muuu?")
print("\u0332".join("LAS"), "vacas")
os.system('pause')
imagen3 = cv2.imread('3.png')
cv2.imshow('Logo OpenCV',imagen3)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp2 = input("Escriba la respuesta del niño (LAS): ")
os.system('cls')

print("Sección B: Clíticos")
os.system('pause')

print("Ejemplo: ")
print("Aquí la niña tiene una guitarra. ¿Qué hace con ella? (Esperar la respuesta del niño, si no la dice entonces se da la respuesta)")
print("\u0332".join("LA"), "toca / (está) tocándo", "\u0332".join("LA"), "/", "\u0332".join("LA"), "va a tocar / (va a) tocar", "\u0332".join("LA"))
os.system('pause')
imagen4 = cv2.imread('4.png')
cv2.imshow('Logo OpenCV',imagen4)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system('pause')

print("3. ¿Qué le va a hacer la niña a la flor?")
print("\u0332".join("LA"), "va a cortar / cortar", "\u0332".join("LA"), "/ (está) cortándo", "\u0332".join("LA"))
os.system('pause')
imagen5 = cv2.imread('5.png')
cv2.imshow('Logo OpenCV',imagen5)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp3 = input("Escriba la respuesta del niño (LA): ")

print("4. ¿Qué hizo el señor con los peces?")
print("\u0332".join("LOS"), "pescó, sacó, guardó, puso / guardándo", "\u0332".join("LOS"), "/ secándo", "\u0332".join("LOS"), "etcétera")
os.system('pause')
imagen6 = cv2.imread('6.png')
cv2.imshow('Logo OpenCV',imagen6)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp4 = input("Escriba la respuesta del niño (LOS): ")

print("5. ¿Qué hace la niña con la moneda?")
print("\u0332".join("LA"), "guarda /", "\u0332".join("LA"), "mete /", "\u0332".join("LA"), "va a guardar, meter / va a guardar", "\u0332".join("LA"), "etcétera")
os.system('pause')
imagen7 = cv2.imread('7.png')
cv2.imshow('Logo OpenCV',imagen7)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp5 = input("Escriba la respuesta del niño (LA): ")
os.system('cls')

print("Sección C: Preposiciones")
os.system('pause')

print("Ejemplo: ")
print("¿Dónde va a pasar el niño? (Esperar la respuesta del niño, si no la dice entonces se da la respuesta)")
print("\u0332".join("POR"), "un tubo / túnel / tronco /", "\u0332".join("POR"), "allí")
os.system('pause')
imagen8 = cv2.imread('8.png')
cv2.imshow('Logo OpenCV',imagen8)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system('pause')
           
print("6. ¿Dónde pegó la foto?")
print("\u0332".join("EN"), "el libro / libreta / álbum, etcétera")
os.system('pause')
imagen9 = cv2.imread('9.png')
cv2.imshow('Logo OpenCV',imagen9)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp6 = input("Escriba la respuesta del niño (EN): ")

print("7. La cuchara sirve...")
print("\u0332".join("PARA"), "comer")
os.system('pause')
imagen10 = cv2.imread('10.png')
cv2.imshow('Logo OpenCV',imagen10)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp7 = input("Escriba la respuesta del niño (PARA): ")

print("8. ¿Dónde fueron los niños?")
print("\u0332".join("A"), "la fiesta /", "\u0332".join("A"), "jugar /", "\u0332".join("AL"), "parque /", "\u0332".join("AL"), "patio, etcétera")
os.system('pause')
imagen11 = cv2.imread('11.png')
cv2.imshow('Logo OpenCV',imagen11)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp8 = input("Escriba la respuesta del niño (A, AL): ")
os.system('cls')

print("Sección D: DERIVATIVOS PARTE 1")
os.system('pause')

print("Ejemplo: ")
print("Mira, este señor está arreglando el jardín. Es un...(Esperar la respuesta del niño, si no la dice entonces se da la respuesta)")
print("jardin", "\u0332".join("ERO"), "/ jardin", "\u0332".join("ADOR"), "(Aceptar cualquier palabra real o inventada que termine con -ero o con -ador")
os.system('pause')
imagen12 = cv2.imread('12.png')
cv2.imshow('Logo OpenCV',imagen12)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system('pause')

print("9. Este señor pesca y es un...")
print("pesc", "\u0332".join("ADOR"), "/ pescad", "\u0332".join("ERO"))
os.system('pause')
imagen13 = cv2.imread('13.png')
cv2.imshow('Logo OpenCV',imagen13)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp9 = input("Escriba la respuesta del niño (ADOR, ERO): ")

print("10. Esta señora plancha y es una...")
print("planch", "\u0332".join("ADORA"), "/ planch", "\u0332".join("ADERA"))
os.system('pause')
imagen14 = cv2.imread('14.png')
cv2.imshow('Logo OpenCV',imagen14)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp10 = input("Escriba la respuesta del niño (ADORA, ADERA): ")
os.system('cls')

print("Sección D: DERIVATIVOS PARTE 2")
os.system('pause')

print("Ejemplo: ")
print("Mira, este señor se enojó. ¿Cómo está?...(Esperar la respuesta del niño, si no la dice entonces se da la respuesta)")
print("enoj", "\u0332".join("ADO"), "/ ard", "\u0332".join("IDO"), "/ confund", "\u0332".join("IDO"), ", etcétera. (Debe ser una palabra real con terminación -ado, -ido, -ada, -ida")
os.system('pause')
imagen15 = cv2.imread('15.png')
cv2.imshow('Logo OpenCV',imagen15)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.system('pause')

print("11. Alguien prendió el foco. ¿Cómo está el foco? Está...")
print("prend", "\u0332".join("IDO"), "/ encend", "\u0332".join("IDO"), "/ apag", "\u0332".join("ADO"))
os.system('pause')
imagen16 = cv2.imread('16.png')
cv2.imshow('Logo OpenCV',imagen16)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp11 = input("Escriba la respuesta del niño (IDO, ADO): ")

print("12. Este chico se asustó. ¿Cómo está? Está...")
print("asust", "\u0332".join("ADO"), "/ sorprend", "\u0332".join("IDO"), "/ enoj", "\u0332".join("ADO"), ", etcétera")
os.system('pause')
imagen17 = cv2.imread('17.png')
cv2.imshow('Logo OpenCV',imagen17)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp12 = input("Escriba la respuesta del niño (IDO, ADO): ")

print("13. Esta señora se tapó. ¿Cómo está? Está...")
print("tap", "\u0332".join("ADA"), "/ asust", "\u0332".join("ADA"), "/ enoj", "\u0332".join("ADA"))
os.system('pause')
imagen18 = cv2.imread('18.png')
cv2.imshow('Logo OpenCV',imagen18)
cv2.waitKey(0)
cv2.destroyAllWindows()
resp13 = input("Escriba la respuesta del niño (ADA): ")
os.system('cls')

print("Repetición de oraciones")
print("En esta segunda sección incluye 12 oraciones divididas en 43 casillas según la complejidad y la longitud de cada oración")
print("Contiene dos ejemplos de práctica para presentar las 12 oraciones y están conformados por oraciones simples (sin argumento) para que el niño se familiarice con las de la tarea que deberá repetir.")
print("Las oraciones siguen el orden canónico de Sujeto (S), Verbo (V) y Objeto (O), ya sea Obeto Directo (OD) u Objeto Indirecto (OI). Además, éstas tienen varios tipos de 'S' que van desde frases nominales con un sustantivo común, hasta nombres propios.")
print("Las frases nominales contienen artículos posesivos y demostrativos, tanto en singular como en plural.")
print("Las frases verbales están compuestas en tiempos verbales como presente, pretérito y perífrasis verbales.")
print("Para construir oraciones complejas se incluyeron los 'ODs' y 'OIs'")
os.system('pause')
os.system('cls')

print("Instrucción: Te voy a decir unas oraciones y quiero que me las digas igual que yo")
print("Práctica 1: [El oso] [duerme mucho]")
print("Práctica 2: [Los niños] [se cayeron ayer]")
os.system('pause')
print("A partir de aquí se evaluará al niño, un total de aciertos de 43, después de cada oración anotar la cantidad de aciertos de acuerdo a la cantidad de partes de cada oración repetidas correctamente")
print("De preferencia, para posteriores evaluaciones escribir la forma en la que repitió la oración el niño")
os.system('pause')
os.system('cls')

print("1. [Los niños pequeños] [no le hacen caso] [a su mamá]")
res1 = input("Cantidad de aciertos /3: ")
r1 = int(res1)
oracion1 = input("Repetición del niño: ")
os.system('cls')

print("2. [El mono feo] [le quitó] [la comida] [al niño]")
res2 = input("Cantidad de aciertos /4: ")
r2 = int(res2)
oracion2 = input("Repetición del niño: ")
os.system('cls')

print("3. [Esas] [son] [las canciones] [que se aprendió] [la nena]")
res3 = input("Cantidad de aciertos /5: ")
r3 = int(res3)
oracion3 = input("Repetición del niño: ")
os.system('cls')

print("4. [Bety] [quiere ponerle] [salsa] [a su comida]")
res4 = input("Cantidad de aciertos /4: ")
r4 = int(res4)
oracion4 = input("Repetición del niño: ")
os.system('cls')

print("5. [Ese gato] [que compraron] [ha crecido mucho]")
res5 = input("Cantidad de aciertos /3: ")
r5 = int(res5)
oracion5 = input("Repetición del niño: ")
os.system('cls')

print("6. [El perro] [que viste en la calle] [es mío]")
res6 = input("Cantidad de aciertos /3: ")
r6 = int(res6)
oracion6 = input("Repetición del niño: ")
os.system('cls')

print("7. [María] [se lava] [la cara]")
res7 = input("Cantidad de aciertos /3: ")
r7 = int(res7)
oracion7 = input("Repetición del niño: ")
os.system('cls')

print("8. [Nuestro abuelo] [toca] [la guitarra]")
res8 = input("Cantidad de aciertos /3: ")
r8 = int(res8)
oracion8 = input("Repetición del niño: ")
os.system('cls')

print("9. [José] [se cortó] [el dedo]")
res9 = input("Cantidad de aciertos /3: ")
r9 = int(res9)
oracion9 = input("Repetición del niño: ")
os.system('cls')

print("10. [Unos niños] [mojaron] [la ropa] [con la manguera]")
res10 = input("Cantidad de aciertos /4: ")
r10 = int(res10)
oracion10 = input("Repetición del niño: ")
os.system('cls')

print("11. [Mi hermana] [tiró] [la leche] [en el piso]")
res11 = input("Cantidad de aciertos /4: ")
r11 = int(res11)
oracion11 = input("Repetición del niño: ")
os.system('cls')

print("12. [La niña] [sacó] [la muñeca] [de la caja]")
res12 = input("Cantidad de aciertos /4: ")
r12 = int(res12)
oracion12 = input("Repetición del niño: ")

#Se suman al contador cada que el niño da una respuesta como la esperada, cada que se responde correctamente se agrega un punto el cual al final obtendrá un porcentaje
if resp1 == 'LOS' or resp1 == 'UNOS':
    cont +=1
if resp2 == 'LAS':
    cont +=1
if resp3 == 'LA':
    cont +=1
if resp4 == 'LOS':
    cont +=1
if resp5 == 'LA':
    cont +=1
if resp6 == 'EN':
    cont +=1
if resp7 == 'PARA':
    cont +=1
if resp8 == 'A' or resp8 == 'AL':
    cont +=1
if resp9 == 'ADOR' or resp9 == 'ERO':
    cont +=1
if resp10 == 'ADORA' or resp10 == 'ADERA':
    cont +=1
if resp11 == 'IDO' or resp11 == 'ADO':
    cont +=1
if resp12 == 'IDO' or resp12 == 'ADO':
    cont +=1
if resp13 == 'ADA':
    cont +=1

cont2 = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12
contT = cont + cont2
porcM = (100 * cont) / 13
porcR = (100 * cont2) / 43
porcT = (porcM + porcR) / 2

os.system('pause')
os.system('cls')

#Obtención de los resultados
print("Nombre:", nombre)
print("Edad:", edad, "con", meses, "meses")
print("Fecha:", dia, "/", mes, "/", anho)
print("Lugar:", lugar)
print("Puntaje crudo")
print("TPL Morfología: ", cont, "/13")
print("Repetición de oraciones: ", cont2, "/43")
print("TPL Global: ", contT)
print("Resultado %")
print("TPL Morfología: ", porcM, "%")
print("Repetición de oraciones: ", porcR, "%")
print("TPL Global: ", porcT, "%")

print("TEL (Transtorno Específico del Lenguaje)")

if edadRango >= 3 and edadRango < 4:
    if mesesRango <= 5:
        if porcT >= 96:
            print("Probabilidad de TEL: 1%")
        if porcT >= 91 and porcT <= 95:
            print("Probabilidad de TEL: 2%")
        if porcT >= 88 and porcT <= 90:
            print("Probabilidad de TEL: 3%")
        if porcT >= 86 and porcT <= 87:
            print("Probabilidad de TEL: 4%")
        if porcT >= 84 and porcT <= 85:
            print("Probabilidad de TEL: 5%")
        if porcT >= 82 and porcT <= 83:
            print("Probabilidad de TEL: 6%")
        if porcT == 81:
            print("Probabilidad de TEL: 7%")
        if porcT == 80:
            print("Probabilidad de TEL: 8%")
        if porcT == 79:
            print("Probabilidad de TEL: 9%")
        if porcT == 78:
            print("Probabilidad de TEL: 10%")
        if porcT == 77:
            print("Probabilidad de TEL: 11%")
        if porcT == 76:
            print("Probabilidad de TEL: 12%")
        if porcT == 75:
            print("Probabilidad de TEL: 13%")
        if porcT == 74:
            print("Probabilidad de TEL: 15%")
        if porcT == 73:
            print("Probabilidad de TEL: 16%")
        if porcT == 72:
            print("Probabilidad de TEL: 18%")
        if porcT == 71:
            print("Probabilidad de TEL: 19%")
        if porcT == 70:
            print("Probabilidad de TEL: 21%")
        if porcT == 69:
            print("Probabilidad de TEL: 23%")
        if porcT == 68:
            print("Probabilidad de TEL: 25%")
        if porcT == 67:
            print("Probabilidad de TEL: 27%")
        if porcT == 66:
            print("Probabilidad de TEL: 30%")
        if porcT == 65:
            print("Probabilidad de TEL: 32%")
        if porcT == 64:
            print("Probabilidad de TEL: 35%")
        if porcT == 63:
            print("Probabilidad de TEL: 37%")
        if porcT == 62:
            print("Probabilidad de TEL: 40%")
        if porcT == 61:
            print("Probabilidad de TEL: 43%")
        if porcT == 60:
            print("Probabilidad de TEL: 45%")
        if porcT == 59:
            print("Probabilidad de TEL: 48%")
        if porcT == 58:
            print("Probabilidad de TEL: 51%")
        if porcT == 57:
            print("Probabilidad de TEL: 54%")
        if porcT == 56:
            print("Probabilidad de TEL: 57%")
        if porcT == 55:
            print("Probabilidad de TEL: 59%")
        if porcT == 54:
            print("Probabilidad de TEL: 62%")
        if porcT == 53:
            print("Probabilidad de TEL: 65%")
        if porcT == 52:
            print("Probabilidad de TEL: 67%")
        if porcT == 51:
            print("Probabilidad de TEL: 70%")
        if porcT == 50:
            print("Probabilidad de TEL: 72%")
        if porcT == 49:
            print("Probabilidad de TEL: 74%")
        if porcT == 48:
            print("Probabilidad de TEL: 76%")
        if porcT == 47:
            print("Probabilidad de TEL: 78%")
        if porcT == 46:
            print("Probabilidad de TEL: 80%")
        if porcT == 45:
            print("Probabilidad de TEL: 82%")
        if porcT == 44:
            print("Probabilidad de TEL: 84%")
        if porcT == 43:
            print("Probabilidad de TEL: 85%")
        if porcT == 42:
            print("Probabilidad de TEL: 86%")
        if porcT == 41:
            print("Probabilidad de TEL: 88%")
        if porcT == 40:
            print("Probabilidad de TEL: 89%")
        if porcT == 39:
            print("Probabilidad de TEL: 90%")
        if porcT == 38:
            print("Probabilidad de TEL: 91%")
        if porcT == 37:
            print("Probabilidad de TEL: 92%")
        if porcT >= 35 and porcT <= 36:
            print("Probabilidad de TEL: 93%")
        if porcT == 34:
            print("Probabilidad de TEL: 94%")
        if porcT >= 32 and porcT <= 33:
            print("Probabilidad de TEL: 95%")
        if porcT >= 30 and porcT <= 31:
            print("Probabilidad de TEL: 96%")
        if porcT >= 27 and porcT <= 29:
            print("Probabilidad de TEL: 97%")
        if porcT >= 22 and porcT <= 26:
            print("Probabilidad de TEL: 98%")
        if porcT >= 13 and porcT <= 21:
            print("Probabilidad de TEL: 99%")
        if porcT <= 12:
            print("Probabilidad de TEL: 100%")
    if mesesRango >= 6 and mesesRango <= 5:
        if porcT >= 89:
            print("Probabilidad de TEL: 0%")
        if porcT >= 83 and porcT <= 88:
            print("Probabilidad de TEL: 1%")
        if porcT >= 80 and porcT <= 82:
            print("Probabilidad de TEL: 2%")
        if porcT >= 78 and porcT <= 79:
            print("Probabilidad de TEL: 3%")
        if porcT == 77:
            print("Probabilidad de TEL: 4%")
        if porcT == 76:
            print("Probabilidad de TEL: 5%")
        if porcT == 75:
            print("Probabilidad de TEL: 6%")
        if porcT == 74:
            print("Probabilidad de TEL: 7%")
        if porcT == 73:
            print("Probabilidad de TEL: 9%")
        if porcT == 72:
            print("Probabilidad de TEL: 11%")
        if porcT == 71:
            print("Probabilidad de TEL: 13%")
        if porcT == 70:
            print("Probabilidad de TEL: 15%")
        if porcT == 69:
            print("Probabilidad de TEL: 18%")
        if porcT == 68:
            print("Probabilidad de TEL: 21%")
        if porcT == 67:
            print("Probabilidad de TEL: 25%")
        if porcT == 66:
            print("Probabilidad de TEL: 28%")
        if porcT == 65:
            print("Probabilidad de TEL: 33%")
        if porcT == 64:
            print("Probabilidad de TEL: 37%")
        if porcT == 63:
            print("Probabilidad de TEL: 42%")
        if porcT == 62:
            print("Probabilidad de TEL: 47%")
        if porcT == 61:
            print("Probabilidad de TEL: 52%")
        if porcT == 60:
            print("Probabilidad de TEL: 57%")
        if porcT == 59:
            print("Probabilidad de TEL: 62%")
        if porcT == 58:
            print("Probabilidad de TEL: 67%")
        if porcT == 57:
            print("Probabilidad de TEL: 71%")
        if porcT == 56:
            print("Probabilidad de TEL: 75%")
        if porcT == 55:
            print("Probabilidad de TEL: 79%")
        if porcT == 54:
            print("Probabilidad de TEL: 82%")
        if porcT == 53:
            print("Probabilidad de TEL: 85%")
        if porcT == 52:
            print("Probabilidad de TEL: 87%")
        if porcT == 51:
            print("Probabilidad de TEL: 89%")
        if porcT == 50:
            print("Probabilidad de TEL: 91%")
        if porcT == 49:
            print("Probabilidad de TEL: 92%")
        if porcT == 48:
            print("Probabilidad de TEL: 94%")
        if porcT == 47:
            print("Probabilidad de TEL: 95%")
        if porcT == 46:
            print("Probabilidad de TEL: 96%")
        if porcT >= 44 and porcT <= 45:
            print("Probabilidad de TEL: 97%")
        if porcT >= 41 and porcT <= 43:
            print("Probabilidad de TEL: 98%")
        if porcT >= 36 and porcT <= 40:
            print("Probabilidad de TEL: 99%")
        if porcT <= 35:
            print("Probabilidad de TEL: 100%")

if edadRango >= 4 and edadRango < 5:
    if mesesRango <= 5:
        if porcT >= 95:
            print("Probabilidad de TEL: 1%")
        if porcT >= 91 and porcT <= 94:
            print("Probabilidad de TEL: 2%")
        if porcT >= 89 and porcT <= 90:
            print("Probabilidad de TEL: 3%")
        if porcT >= 87 and porcT <= 88:
            print("Probabilidad de TEL: 4%")
        if porcT >= 85 and porcT <= 86:
            print("Probabilidad de TEL: 5%")
        if porcT == 84:
            print("Probabilidad de TEL: 6%")
        if porcT == 83:
            print("Probabilidad de TEL: 7%")
        if porcT == 82:
            print("Probabilidad de TEL: 8%")
        if porcT == 81:
            print("Probabilidad de TEL: 9%")
        if porcT == 80:
            print("Probabilidad de TEL: 10%")
        if porcT == 79:
            print("Probabilidad de TEL: 12%")
        if porcT == 78:
            print("Probabilidad de TEL: 13%")
        if porcT == 77:
            print("Probabilidad de TEL: 15%")
        if porcT == 76:
            print("Probabilidad de TEL: 17%")
        if porcT == 75:
            print("Probabilidad de TEL: 19%")
        if porcT == 74:
            print("Probabilidad de TEL: 21%")
        if porcT == 73:
            print("Probabilidad de TEL: 24%")
        if porcT == 72:
            print("Probabilidad de TEL: 27%")
        if porcT == 71:
            print("Probabilidad de TEL: 29%")
        if porcT == 70:
            print("Probabilidad de TEL: 32%")
        if porcT == 69:
            print("Probabilidad de TEL: 36%")
        if porcT == 68:
            print("Probabilidad de TEL: 39%")
        if porcT == 67:
            print("Probabilidad de TEL: 42%")
        if porcT == 66:
            print("Probabilidad de TEL: 46%")
        if porcT == 65:
            print("Probabilidad de TEL: 49%")
        if porcT == 64:
            print("Probabilidad de TEL: 53%")
        if porcT == 63:
            print("Probabilidad de TEL: 56%")
        if porcT == 62:
            print("Probabilidad de TEL: 60%")
        if porcT == 61:
            print("Probabilidad de TEL: 63%")
        if porcT == 60:
            print("Probabilidad de TEL: 66%")
        if porcT == 59:
            print("Probabilidad de TEL: 70%")
        if porcT == 58:
            print("Probabilidad de TEL: 72%")
        if porcT == 57:
            print("Probabilidad de TEL: 75%")
        if porcT == 56:
            print("Probabilidad de TEL: 78%")
        if porcT == 55:
            print("Probabilidad de TEL: 80%")
        if porcT == 54:
            print("Probabilidad de TEL: 82%")
        if porcT == 53:
            print("Probabilidad de TEL: 84%")
        if porcT == 52:
            print("Probabilidad de TEL: 86%")
        if porcT == 51:
            print("Probabilidad de TEL: 88%")
        if porcT == 50:
            print("Probabilidad de TEL: 89%")
        if porcT == 49:
            print("Probabilidad de TEL: 90%")
        if porcT == 48:
            print("Probabilidad de TEL: 92%")
        if porcT == 47:
            print("Probabilidad de TEL: 93%")
        if porcT >= 45 and porcT <= 46:
            print("Probabilidad de TEL: 94%")
        if porcT == 44:
            print("Probabilidad de TEL: 95%")
        if porcT >= 42 and porcT <= 43:
            print("Probabilidad de TEL: 96%")
        if porcT >= 40 and porcT <= 41:
            print("Probabilidad de TEL: 97%")
        if porcT >= 36 and porcT <= 39:
            print("Probabilidad de TEL: 98%")
        if porcT >= 29 and porcT <= 35:
            print("Probabilidad de TEL: 99%")
        if porcT <= 28:
            print("Probabilidad de TEL: 100%")
    if mesesRango >= 6 and mesesRango <= 5:
        if porcT >= 95:
            print("Probabilidad de TEL: 1%")
        if porcT >= 92 and porcT <= 94:
            print("Probabilidad de TEL: 2%")
        if porcT >= 89 and porcT <= 91:
            print("Probabilidad de TEL: 3%")
        if porcT == 88:
            print("Probabilidad de TEL: 4%")
        if porcT >= 86 and porcT <= 87:
            print("Probabilidad de TEL: 5%")
        if porcT == 85:
            print("Probabilidad de TEL: 6%")
        if porcT == 84:
            print("Probabilidad de TEL: 7%")
        if porcT == 83:
            print("Probabilidad de TEL: 8%")
        if porcT == 82:
            print("Probabilidad de TEL: 10%")
        if porcT == 81:
            print("Probabilidad de TEL: 11%")
        if porcT == 80:
            print("Probabilidad de TEL: 13%")
        if porcT == 79:
            print("Probabilidad de TEL: 14%")
        if porcT == 78:
            print("Probabilidad de TEL: 17%")
        if porcT == 77:
            print("Probabilidad de TEL: 19%")
        if porcT == 76:
            print("Probabilidad de TEL: 21%")
        if porcT == 75:
            print("Probabilidad de TEL: 24%")
        if porcT == 74:
            print("Probabilidad de TEL: 27%")
        if porcT == 73:
            print("Probabilidad de TEL: 30%")
        if porcT == 72:
            print("Probabilidad de TEL: 34%")
        if porcT == 71:
            print("Probabilidad de TEL: 37%")
        if porcT == 70:
            print("Probabilidad de TEL: 41%")
        if porcT == 69:
            print("Probabilidad de TEL: 45%")
        if porcT == 68:
            print("Probabilidad de TEL: 49%")
        if porcT == 67:
            print("Probabilidad de TEL: 53%")
        if porcT == 66:
            print("Probabilidad de TEL: 57%")
        if porcT == 65:
            print("Probabilidad de TEL: 61%")
        if porcT == 64:
            print("Probabilidad de TEL: 64%")
        if porcT == 63:
            print("Probabilidad de TEL: 68%")
        if porcT == 62:
            print("Probabilidad de TEL: 71%")
        if porcT == 61:
            print("Probabilidad de TEL: 74%")
        if porcT == 60:
            print("Probabilidad de TEL: 77%")
        if porcT == 59:
            print("Probabilidad de TEL: 80%")
        if porcT == 58:
            print("Probabilidad de TEL: 82%")
        if porcT == 57:
            print("Probabilidad de TEL: 84%")
        if porcT == 56:
            print("Probabilidad de TEL: 86%")
        if porcT == 55:
            print("Probabilidad de TEL: 88%")
        if porcT == 54:
            print("Probabilidad de TEL: 90%")
        if porcT == 53:
            print("Probabilidad de TEL: 91%")
        if porcT == 52:
            print("Probabilidad de TEL: 92%")
        if porcT == 51:
            print("Probabilidad de TEL: 93%")
        if porcT == 50:
            print("Probabilidad de TEL: 94%")
        if porcT == 49:
            print("Probabilidad de TEL: 95%")
        if porcT >= 47 and porcT <= 48:
            print("Probabilidad de TEL: 96%")
        if porcT >= 45 and porcT <= 46:
            print("Probabilidad de TEL: 97%")
        if porcT >= 42 and porcT <= 44:
            print("Probabilidad de TEL: 98%")
        if porcT >= 35 and porcT <= 41:
            print("Probabilidad de TEL: 99%")
        if porcT <= 34:
            print("Probabilidad de TEL: 100%")      

if edadRango >= 5 and edadRango <= 6:
    if porcT >= 98:
        print("Probabilidad de TEL: 2%")
    if porcT >= 95 and porcT <= 97:
        print("Probabilidad de TEL: 3%")
    if porcT == 94:
        print("Probabilidad de TEL: 4%")
    if porcT >= 92 and porcT <= 93:
        print("Probabilidad de TEL: 5%")
    if porcT == 91:
        print("Probabilidad de TEL: 6%")
    if porcT == 90:
        print("Probabilidad de TEL: 7%")
    if porcT == 89:
        print("Probabilidad de TEL: 8%")
    if porcT == 88:
        print("Probabilidad de TEL: 9%")
    if porcT == 87:
        print("Probabilidad de TEL: 10%")
    if porcT == 86:
        print("Probabilidad de TEL: 11%")
    if porcT == 85:
        print("Probabilidad de TEL: 12%")
    if porcT == 84:
        print("Probabilidad de TEL: 14%")
    if porcT == 83:
        print("Probabilidad de TEL: 16%")
    if porcT == 82:
        print("Probabilidad de TEL: 17%")
    if porcT == 81:
        print("Probabilidad de TEL: 19%")
    if porcT == 80:
        print("Probabilidad de TEL: 22%")
    if porcT == 79:
        print("Probabilidad de TEL: 24%")
    if porcT == 78:
        print("Probabilidad de TEL: 27%")
    if porcT == 77:
        print("Probabilidad de TEL: 29%")
    if porcT == 76:
        print("Probabilidad de TEL: 32%")
    if porcT == 75:
        print("Probabilidad de TEL: 35%")
    if porcT == 74:
        print("Probabilidad de TEL: 39%")
    if porcT == 73:
        print("Probabilidad de TEL: 42%")
    if porcT == 72:
        print("Probabilidad de TEL: 45%")
    if porcT == 71:
        print("Probabilidad de TEL: 49%")
    if porcT == 70:
        print("Probabilidad de TEL: 52%")
    if porcT == 69:
        print("Probabilidad de TEL: 55%")
    if porcT == 68:
        print("Probabilidad de TEL: 59%")
    if porcT == 67:
        print("Probabilidad de TEL: 62%")
    if porcT == 66:
        print("Probabilidad de TEL: 65%")
    if porcT == 65:
        print("Probabilidad de TEL: 68%")
    if porcT == 64:
        print("Probabilidad de TEL: 71%")
    if porcT == 63:
        print("Probabilidad de TEL: 74%")
    if porcT == 62:
        print("Probabilidad de TEL: 76%")
    if porcT == 61:
        print("Probabilidad de TEL: 79%")
    if porcT == 60:
        print("Probabilidad de TEL: 81%")
    if porcT == 59:
        print("Probabilidad de TEL: 83%")
    if porcT == 58:
        print("Probabilidad de TEL: 85%")
    if porcT == 57:
        print("Probabilidad de TEL: 87%")
    if porcT == 56:
        print("Probabilidad de TEL: 88%")
    if porcT == 55:
        print("Probabilidad de TEL: 89%")
    if porcT == 54:
        print("Probabilidad de TEL: 91%")
    if porcT == 53:
        print("Probabilidad de TEL: 92%")
    if porcT == 52:
        print("Probabilidad de TEL: 93%")
    if porcT >= 50 and porcT <= 51:
        print("Probabilidad de TEL: 94%")
    if porcT == 49:
        print("Probabilidad de TEL: 95%")
    if porcT >= 47 and porcT <= 48:
        print("Probabilidad de TEL: 96%")
    if porcT >= 44 and porcT <= 46:
        print("Probabilidad de TEL: 97%")
    if porcT >= 41 and porcT <= 43:
        print("Probabilidad de TEL: 98%")
    if porcT >= 33 and porcT <= 40:
        print("Probabilidad de TEL: 99%")
    if porcT <= 32:
        print("Probabilidad de TEL: 100%")

if edadRango >= 6:
    if porcT >= 98:
        print("Probabilidad de TEL: 0%")
    if porcT >= 94 and porcT <= 97:
        print("Probabilidad de TEL: 1%")
    if porcT == 93:
        print("Probabilidad de TEL: 2%")
    if porcT == 92:
        print("Probabilidad de TEL: 3%")
    if porcT == 91:
        print("Probabilidad de TEL: 4%")
    if porcT == 90:
        print("Probabilidad de TEL: 5%")
    if porcT == 89:
        print("Probabilidad de TEL: 7%")
    if porcT == 88:
        print("Probabilidad de TEL: 9%")
    if porcT == 87:
        print("Probabilidad de TEL: 13%")
    if porcT == 86:
        print("Probabilidad de TEL: 17%")
    if porcT == 85:
        print("Probabilidad de TEL: 22%")
    if porcT == 84:
        print("Probabilidad de TEL: 28%")
    if porcT == 83:
        print("Probabilidad de TEL: 36%")
    if porcT == 82:
        print("Probabilidad de TEL: 43%")
    if porcT == 81:
        print("Probabilidad de TEL: 52%")
    if porcT == 80:
        print("Probabilidad de TEL: 60%")
    if porcT == 79:
        print("Probabilidad de TEL: 68%")
    if porcT == 78:
        print("Probabilidad de TEL: 74%")
    if porcT == 77:
        print("Probabilidad de TEL: 80%")
    if porcT == 76:
        print("Probabilidad de TEL: 85%")
    if porcT == 75:
        print("Probabilidad de TEL: 89%")
    if porcT == 74:
        print("Probabilidad de TEL: 92%")
    if porcT == 73:
        print("Probabilidad de TEL: 94%")
    if porcT == 72:
        print("Probabilidad de TEL: 96%")
    if porcT == 71:
        print("Probabilidad de TEL: 97%")
    if porcT >= 69 and porcT <= 70:
        print("Probabilidad de TEL: 98%")
    if porcT >= 66 and porcT <= 68:
        print("Probabilidad de TEL: 99%")
    if porcT <= 65:
        print("Probabilidad de TEL: 100%")

print("Respuestas de morfología y anotaciones de la repetición de ", nombre, ":")
print(resp1, resp2, resp3, resp4, resp5, resp6, resp7, resp8, resp9, resp10, resp11, resp12, resp13)
print(oracion1)
print(oracion2)
print(oracion3)
print(oracion4)
print(oracion5)
print(oracion6)
print(oracion7)
print(oracion8)
print(oracion9)
print(oracion10)
print(oracion11)
print(oracion12)
os.system('pause')
