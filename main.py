# Principal
# Por: Santiago, L. D.

from TOOLS import toolp as tls
from TOOLS import historia as his
from inflexiones import inflexion1 as flx
from inflexiones import needfile
from TOOLS.texto_print import textjust

justificado = 75 # Justificación del texto

def main():
	heroin = "" # Inicializamos para evitar errores
	prota = ""
	if needfile.ok(): # Revisamos que todo esté en orden
		pass
	else:
		print("Error con ficheros TXT/. Archivos necesarios no existen.")
		return

	# Presentación

	his.portada()			# Imprime portada
	prota = tls.protaname()	# Pide nombre del protagonista
	print()

	# Introducción

	print("*****Primera parte: Introducción.*****\n")

	archivo = "TXT/Intro.txt"
	NumLineas = tls.contarlineas(archivo)
	intro = open(archivo, "r")				# Imprimimos la introducción con
	for i in range(NumLineas):				# determinadas pausas
		parrafo=tls.segmento(prota,heroin,intro.readline())
		textjust(parrafo,justificado,"\n")
		if i == 3:
			tls.pausa()
		elif i == 5:
			tls.pausa()
			heroin = tls.heroinname(prota)	# En algún momento se pide nombre de
			print()							# protagonista femenina, también llamada
		elif i == 9:						# heroína
			tls.pausa()
	intro.close()

	tls.pausa()

	# Desarrollo

	print("*****Segunda parte: Desarrollo.*****\n")
# -------------------------Intrucciones-------------------------------------------------------
	control = his.intrucciones(prota, heroin, "TXT/control.txt")
# --------------------------------------------------------------------------------------------
	tls.pausa()
	archivo = "TXT/desarrollo.txt"  		# Imprimimos archivo correspondiente al desarrollo
	flx.imprimir(prota, heroin, archivo)	# de la historia

	# primer punto de inflexión

	eleccion1 = his.menu("ab")				# Imprime el segmento de la historia correspodiente
	flx.inflex(prota, heroin, [eleccion1])	# a la primera elección

	# segundo punto de inflexion y final
	if eleccion1 == 1:
		op = "abc"
	else:
		op = "ab"

	eleccion2 = his.menu(op)									# Imprime el segmento de la historia correspodiente
	ruta = flx.inflex(prota, heroin, [eleccion1,eleccion2])		# a la segunda eleccion, tomando en cuenta también
																# la primera
	acum_ruta, acum_heroes = flx.confcontrol(prota,heroin,control,"TXT/control.txt",ruta)
	his.RegLOGROS(acum_ruta,acum_heroes)
	his.creditos()

if __name__ == '__main__':
	main()

