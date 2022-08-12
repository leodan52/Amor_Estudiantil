# Texto en pantalla
# Desarrollo de herramientas que facilitan la impresión en pantalla
# Estatus: Continua desarrollando

def texto(cadena,n):
	inicio = 0
	for i in range(len(cadena)):
		if i%n == 0:
			print(cadena[inicio:i])
			inicio = i

	print(cadena[inicio:])

def texto1(cadena,n):
	m = 0
	for i in cadena:
		print(i, end="")
		m += 1
		if m>=n:
			print()
			m = 0
	print()

def enc_caracter(cadena,caracter):
	aux = []
	for i in range(len(cadena)):
		if cadena[i] == caracter:
			aux.append(i)
	return aux

def texto2(cadena,n):
	inicio = 0
	final = n
	control = "loop"
	print("*"*n)
	while control == "loop":
		aux = enc_caracter(cadena[:final]," ")
		print(cadena[inicio:aux[-1]])
		inicio = aux[-1] + 1
		final = inicio + n
		if final > len(cadena)-1:
			control = "exit"
	print(cadena[inicio:])

def textjust(cadena, maxlargo,final):	# Este es el chido para justificar
	cadena1 = cadena.strip()			# Es la unica función que se usa en
	palabras = cadena1.split(" ")		# Amor estudiantil
	aux = 0
	salida = ""
	if cadena1 == "":
		salida = cadena1
	else:
		for p in palabras:
			aux += len(p)
			if aux <= maxlargo:
				salida += p + " "
				aux += 1
			else:
				aux = len(p)+1
				salida += "\n"
				salida += p + " "
	print(salida.strip(), end=final)

def inboxtex(cadena, maxlargo): # Chido, pero en caja
	cadena1 = cadena.strip()
	palabras = cadena1.split(" ")
	aux = 0
	crctr="|"
	aa = "*"*maxlargo
	print(aa)
	print(crctr + " ", end="")
	for p in palabras:
		aux += len(p)
		if aux <= maxlargo-4:
			print(p, end=" ")
			aux += 1
		else:
			s = " "*(maxlargo-aux+len(p)-3)
			print(s + crctr)
			aux = len(p)+1
			print(crctr + " " + p, end=" ")
	s = " "*(maxlargo-aux-3)
	print(s + crctr)
	print(aa)
