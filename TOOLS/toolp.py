# Herramientas particulares
# Por Santiago, L. D.

try:
	from TOOLS import cifrar as cf
except ModuleNotFoundError:
	import cifrar as cf

import sys
from getpass import getpass
import time

def contarlineas(archivo):   # Cuenta las lineas en archivo
	aux = open(archivo, "r")
	n = len(aux.readlines())
	aux.close()
	return n

def pausa():				# Genera una pausa con un mensaje
	print("Presiona enter...", end = "", flush=True)
	aux = getpass(" ")
	sys.stdout.write("\033[F") #back to previous line
	sys.stdout.write("\033[K") #clear line
	return aux

def pausa2():				# pausa sin mensaje
	print(end="", flush=True)
	aux = getpass(" ")
	return aux

def str2list(cadena):		# Convierte una cadena de caracteres
	aux = cadena.strip()	# cuya estructura es idéntica a una lista
	aux2 = []				# a la respectiva lista
							# La entrada es la lectura de los archivos en TXT/
	for i in [ "[", "]", " "]:
		aux = aux.replace(i, "")
	aux = aux.split(",")
	for i in aux:
		aux2.append(eval(i))

	return aux2

def validar(cadena):		# Restringe el uso de caracteres para los nombres
	aux = cadena.strip()
	aux = aux.lower()
	aux = aux.replace(" ", "")
	for i in aux:
		if 97 <= ord(i) <= 122 or ord(i) >= 192 :
			pass
		else:
			return 0
	return 1

def protaname():			# Pide y procesa el nombre del protagonista
	loop = "malo"
	while loop == "malo":
		prota = input("¿Cuál es tu nombre?: ")
		prota = prota.strip()
		if len(prota) > 10:
			print("El nombre es demasiado largo.")
		elif prota == "":
			prota = cf.desencriptar([56, 9, 0, 18, 22, 0, 16])
			break
		elif validar(prota) == 0:
			print("Nombre inválido.")
		else:
			break
	return prota.strip()

def heroinname(prota):		# Pide y procesa el nombre de la heroína
	loop = "malo"
	while loop == "malo":
		heroin = input("Elige el nombre de la heroína: ")
		heroin = heroin.strip()
		if len(heroin) > 10:
			print("El nombre es demasiado largo.")
		elif heroin == "":
			heroin = cf.desencriptar([56, 0, 13, 25, 22, 0])
			break
		elif validar(heroin) == 0:
			print("Nombre inválido.")
		else:
			break
	if (prota == cf.desencriptar([33, 4, 22, 10, 0, 16])		# Esto está cifrado, no lo pienses mucho
		or prota == cf.desencriptar([0, 4, 22, 10, 0, 16])
		or prota == cf.desencriptar([33, 4, 22, 11, 0, 16])
		or prota == cf.desencriptar([45, 9, 18, 23, 5, 14, 10, 16])):
		heroin = cf.desencriptar([43, 22, 15, 0])
	elif prota == cf.desencriptar([48, 0, 22, 3, 18, 23]):
		heroin = cf.desencriptar([56, 18, 7, 10])
	elif prota == cf.desencriptar([47, 5, 18, 16, 0, 22, 4, 18]):
		heroin = cf.desencriptar([53, 0, 15, 5, 14, 0])
	return heroin


def cambiarnombres(prota,heroin,parrafo): 	# Coloca los nombres del prota y la heroína en el
	aux = parrafo.strip()					# texto por los seleccionados por el usuario
	aux = aux.replace("PROTA", prota)		# un parrafo por vez
	aux = aux.replace("HEROIN", heroin)
	return aux


def segmento(prota,heroin,i):				# Procesa el texto completo preescrito de la historia
	if i == "\n" or i == "":				# usando desencritar() para traducir y cambiarnombres()
		aux1= ""							# para el proceso correspondiente
	else:
		aux = str2list(i)
		aux = cf.desencriptar(aux)
		aux1 = cambiarnombres(prota,heroin,aux)

	return aux1

def main():
	print("^[")
	for i in range(10):
		print(i)
		time.sleep(1)
		sys.stdout.write("\033[F") #back to previous line
		sys.stdout.write("\033[K") #clear line


if __name__ == '__main__':
	main()


