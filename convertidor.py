from TOOLS import cifrar as cf
from TOOLS import toolp as tls

def conv():
	mapa = (["Intro.txt","desarrollo.txt", "0.txt",
	"1.txt","01.txt","00.txt","10.txt","11.txt","12.txt", "creditos.txt"])
	for ruta in mapa:
		a_entrada = "AUX/" + ruta
		a_salida = "TXT/" + ruta
		lineas = 0

		n = tls.contarlineas(a_entrada)

		entrada = open(a_entrada,"r")
		salida = open(a_salida,"w")

		for i in range(n):
			parrafo = entrada.readline()
			parrafo = parrafo.strip()
			oculto = cf.encriptar(parrafo)

			print(oculto, file=salida)
			if oculto != "":
				lineas += 1

		print("El archivo", ruta, "tiene", lineas, "lineas", end="")
		print("\tY tiene", n,"lienas con saltos")

		salida.close()
		entrada.close()

conv()
