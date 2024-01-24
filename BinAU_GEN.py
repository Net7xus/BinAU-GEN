import sys
from random import randint
from os import system
import datetime
import random

#usr/python
#Code_by: Nexus
system("chmod 777 BinAU_GEN.py")
system("clear")
print("")
print("\033[1;33m///\033[1;31mBY: \033[1;32mNet7xus")
print("\033[1;34m///\033[1;32m≧◉◡◉≦")
print("")
def pedir_contrasena():
    contrasena = input("\033[1;31m///\033[1;32mIntroduce la contraseña: ")
    return contrasena

contrasena_correcta = "Netxus7774"  # Cambia esta contraseña por la que deseas utilizar

intentos_restantes = 3

while intentos_restantes > 0:
    contraseña_ingresada = pedir_contrasena()
    
    if contraseña_ingresada == contrasena_correcta:
        print("\033[1;33m///\033[1;33mContraseña correcta. Acceso concedido.")
        break
    else:
        intentos_restantes -= 1
        print(f"\033[1;31m///\033[1;34m[\033[1;31m!\033[1;34m]Incorrecta. Te quedan {intentos_restantes} intentos restantes.")

if intentos_restantes == 0:
    print("\033[1;31m///\033[1;31m[x]Has excedido a los intentos. Acceso denegado.")
    exit()

print("")
system("sleep 2")
print("\033[1;34m")
#usr/python
#Code_by: Nexus
system("figlet BinAU")
print ("  \033[1;31m,--^----------,--------,-----,-------^--,;")
print ("  | |||||||||   `--------'     |          O")
print ("  `+---------------------------^----------|")
print ("    `\_,-------, _________________________|")
print ("      / XXXXXX /`|     /")
print ("     / XXXXXX /  `\   /")
print ("    / XXXXXX /\______(")
print ("   / XXXXXX /    ")
print ("  / XXXXXX /")
print (" (________(")
print ("  `------'")
print("\033[1;34m")
system("figlet GEN")

print(" \033[1;31m[×]▪︎▪︎▪︎》 \033[1;34mBinAU_GEN \033[1;31m《▪︎▪︎▪︎[×]")
system("sleep 1")

print("")
cantidad = input(" \033[1;37m[+]Generar: ")
print("")
print("\033[1;31m--------------------------------------")
print("| \033[1;34m    BIN          \033[1;31m|\033[1;34m FECHA \033[1;31m| \033[1;34mSTATUS\033[1;31m  |")
print("\033[1;31m--------------------------------------")

bin_format = "53265552xxxxxxxx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc

def dategen():
  now = datetime.datetime.now()
  date = ""
  month = str(randint(3, 8))
  current_year = str(now.year)
  year = str(random.randint(23, 28))
  date = month + "/" + year

  return date


def main():
  for i in range(int(cantidad)):
    cc = generar_cc(bin_format)
    print(f"\033[1;31m| \033[1;37m{cc} \033[1;31m| \033[1;37m{dategen()}  \033[1;31m| \033[1;37mAPROVED \033[1;31m|")
    print("\033[1;31m--------------------------------------")
main()
print("")
print("")
print("\033[1;34m🌐𝗜𝗣: AUSTRALIA [🇦🇺]")
print("")
print("🔖DIRECCIÓN POSTAL: Broken Arrow Corporation")
print("🔖DEPARTAMENTO: Marley point road")
print("🔖CIUDAD: Mirboo North")
print("🔖PROVINCIA: Mirboo North")
print("🔖ZIP CODE: 3871")
print("🔖PHONE: +61 954324xxxx")
print("")

num = input("Desea generar el Tlf (y/n): ")

if num == "y":
   system("python numero.py")
else:
   exit()

print("")
nombre = input("\033[1;34mDesea generar un nombre random (y/n): ")

if nombre == "y":
    system("python nya.py")
else:
    exit()

print("")
volver = input("\033[1;32mPresione (y) para binear (n) salir: ")

if volver == "y":
    system("bash b_g_.sh")
else:
    exit()
