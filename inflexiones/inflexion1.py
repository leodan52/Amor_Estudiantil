# Motor para administrar las distintas rutas
# que se generan en cada punto de inflexion
# en la historia
# Por: Santiago L. D.

from TOOLS import toolp as tls
from TOOLS.texto_print import textjust

justificado = 75

def imprimir(prota,heroin,archivo):			# Imprime el texto de archivo, procesando
	n = tls.contarlineas(archivo)			# antes con segmento(), ver toolp.py y
											# textjust(), ver texto_print
	entrada = open(archivo, "r")
	for i in range(n):
		parrafo = tls.segmento(prota,heroin,entrada.readline())
		textjust(parrafo,justificado,"")
		if parrafo != "" and parrafo[0] != "*" and parrafo[0] != "(":
			tls.pausa2()
		else:
			print()
	entrada.close()

def inflex(prota,heroin,elec):		# Procesa las elecciones del usuario y genera
	name_file = ""					# el nombre del archivo TXT correspondiente a la ruta
	for i in elec:					# Usa imprimir() para mostrarlo en pantalla
		name_file += str(i)
	archivo = "TXT/" + name_file + ".txt"

	imprimir(prota,heroin,archivo)
	return name_file

def confcontrol(prota,heroin,num,cache,ruta):
	entrada = open(cache, "r")
	lineas = entrada.readlines()
	if lineas[1].find(ruta) == -1:
		linea2 = lineas[1].strip() + ruta + ","
		linea3 = lineas[2].strip() + prota + "." + heroin + ","
	else:
		linea2 = lineas[1].strip()
		linea3 = lineas[2].strip()
	entrada.close()
	salida = open(cache, "w")
	print(num, file=salida)
	print(linea2, file=salida)
	print(linea3, file=salida)
	salida.close()
	return linea2,linea3


