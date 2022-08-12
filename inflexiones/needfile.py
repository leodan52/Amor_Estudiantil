# Gestionar archivos necesarios

nombres = "TXT/historial_nombres.txt"
control = "TXT/control.txt"
historiamapa = (["Intro.txt","desarrollo.txt", "0.txt",
	"1.txt","01.txt","00.txt","10.txt","11.txt","12.txt", "creditos.txt","portada.txt"])

def	ArchivoExist(myfile):
	try:
		f = open(myfile,"r")
		f.close()
		return True
	except FileNotFoundError:
		return False

def Checar(Archivo,linea):
	if ArchivoExist(Archivo):
		pass
	else:
		f = open(Archivo, "w")
		print(linea,file=f)
		f.close()

def ok():
	Checar(nombres,"")
	Checar(control,"0\n\n")

	for i in historiamapa:
		if ArchivoExist("TXT/" + i):
			pass
		else:
			return False

	return True


