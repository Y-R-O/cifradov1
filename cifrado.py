import pyperclip as clipboard

palabra1 = str(input("Introduce palabra para cifrar: "))
palabra = palabra1.lower() #Convertir a minusculas
hola = False

resultado = ""
for x in palabra:
    if x == "a":
        resultado += "Qv3"

    elif x == "b":
        resultado += "Px2"

    elif x == "c":
        resultado += "Za2"
 
    elif x == "d":
        resultado += "Nn3"
 
    elif x == "e":
        resultado += "Bc3"
 
    elif x == "f":
        resultado += "Vm4"
 
    elif x == "g":
        resultado += "Mp5"
 
    elif x == "h":
        resultado += "Av9"
 
    elif x == "i":
        resultado += "Pm4"
 
    elif x == "j":
        resultado += "Te8"
 
    elif x == "k":
        resultado += "Ce2"
 
    elif x == "l":
        resultado += "Bm4"
 
    elif x == "m":
        resultado += "Bf3"
 
    elif x == "n":
        resultado += "Rs9"
 
    elif x == "ñ":
        resultado += "Mx6"
 
    elif x == "o":
        resultado += "Xh7"
 
    elif x == "p":
        resultado += "Yp7"
 
    elif x == "q":
        resultado += "Lu9"
 
    elif x == "r":
        resultado += "Em6"
 
    elif x == "s":
        resultado += "Gf5"
 
    elif x == "t":
        resultado += "Fn3"
 
    elif x == "u":
        resultado += "Gp2"
 
    elif x == "v":
        resultado += "Dn5"
 
    elif x == "x":
        resultado += "Jm2"
 
    elif x == "y":
        resultado += "Wc6"
 
    elif x == "z":
        resultado += "Pj2"
 
    elif x == "1":
        resultado += "Ma5"
 
    elif x == "2":
        resultado += "Yc8"
 
    elif x == "3":
        resultado += "Nm8"
 
    elif x == "4":
        resultado += "Ru4"
 
    elif x == "5":
        resultado += "Wg8"
 
    elif x == "6":
        resultado += "Wq8"
 
    elif x == "7":
        resultado += "Ta4"
 
    elif x == "8":
        resultado += "Cd5"
 
    elif x == "9":
        resultado += "Fc8"
 
    elif x == "0":
        resultado += "Cn4"
 
    elif x == "@":
        resultado += "Hb8"
 
    elif x == "!":
        resultado += "Zk5"
 
    elif x == "-":
        resultado += "Ge7"
 
    elif x == "/":
        resultado += "Yi9"
    elif x == (" "):
        resultado += " "

    elif x == "$":
        hola = True
        
    else: 
        print("ERROR")

if hola == True:
    clipboard.copy(resultado)

print("*"*100)
print(" ")
print(resultado)
print(" ")
print("*"*100)