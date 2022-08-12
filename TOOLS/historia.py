# DesarrolLo de la historia
from TOOLS import cifrar as cf
from TOOLS import toolp as tls
import time, sys

def portada():						# Imprime la portada con el titulo, el subtitulo y el autor
	archivo = "TXT/portada.txt"
	infile = open(archivo, "r")
	mensaje = "".join(infile.readlines())
	print(mensaje)
	infile.close()

def histnames(prota,heroin):
	archivo = "TXT/historial_nombres.txt"
	entrada = open(archivo, "r")
	backhis ="".join(entrada.readlines())
	entrada.close()

	salida = open(archivo, "w")
	print(backhis, end="", file=salida)
	print(prota + ", " + heroin, file=salida)
	salida.close()

def intrucciones(prota, heroin, cache):
	print("[¡Jugador! Elige las opciones correctas para que", prota, "no sea rechazado]")
	print("[Presiona Enter para ir avanzando en la historia.]")
	entrada = open(cache, "r")
	control = eval(entrada.readline().strip())
	if control == 0:
		print("[¡Elige la ruta que tu corazón dicte!]\n")
	else:
		print()
	entrada.close()
	histnames(prota,heroin)
	return control + 1

def control(opciones,eleccion):
	for i in opciones:
		aux = eleccion == i
		if aux:
			return True
	return False

def menu(opciones):					# Administra el menú de elección
	loop = "algo"					# Solo es válido ingresar a o b
	print("Tú elección: ", end="")	# cualquier otro ingreso es negado
	while loop == "algo":
		eleccion = input("")
		eleccion = eleccion.strip().lower()
		if control(opciones,eleccion):
			break
		else:
			print("Elige nuevamente: ", end="")
	print()
	aux = opciones.find(eleccion)
	return aux

def creditos():
	archivo = "TXT/creditos.txt"
	lineas = tls.contarlineas(archivo) - 1
	entrada = open(archivo, "r")
	print()
	for i in range(lineas):
		if	i%2 == 0:
			imprimir = (cf.desencriptar(tls.str2list(entrada.readline()))
						+ "\n\t" + cf.desencriptar(tls.str2list(entrada.readline())) + "\n")
			print(imprimir, flush=True)
			time.sleep(1.5)
		else:
			print("\n\n", flush=True)
			time.sleep(.5)
		if i != lineas - 1:
			for i in range(3):
				sys.stdout.write("\033[F") #back to previous line
				sys.stdout.write("\033[K") #clear line


def RegLOGROS(avance,heroes):
	final = len(avance)
	avance = avance.split(",")
	heroes = heroes.split(",")

	salida = open("LOGROS.txt", "w")

	print("Tus logros:", file=salida)
	for i in range(len(avance)):
		if avance[i] =="":
			break
		elif avance[i] == "00":
			mensaje = cf.desencriptar([4, 5, -1, 14, 0, -1, 53, 5, 14, 5, 0])
		elif avance[i] == "01":
			mensaje = cf.desencriptar([4, 5, 14, -1, 33, 15, 10, 8, 18, -3,
										-1, 40, 10, 16, 0, 14, -1, 15, 0, 14, 18])
		elif avance[i] == "10":
			mensaje = cf.desencriptar([4, 5, 14, -1, 47, 18, 3, 18])
		elif avance[i] == "11":
			mensaje = cf.desencriptar([4, 5, 14, -1, 42, 5, 22, 10, 4, 18])
		elif avance[i] == "12":
			mensaje = cf.desencriptar([4, 5, 14, -1, 57, 18, 16, 24, 18])
		aux = heroes[i].split(".")
		print("Has completado La Ruta " + mensaje
				+ " como " + aux[0] + ". Heroína: " + aux[1], file=salida)
	if final == 15 :
		print("\nHas completado todas las rutas. ¡¡¡Felicidades!!!", file=salida)
	salida.close()
