# Funciones para ocultar mensajes en programas
# Por: Santiago, L. D.
#	  0	   1	  2	 ...  n-1	n
#	-n-1  -n	-n+1	  -2	-1

def llave():
	B="aábcdeéfghiíjklmnñoópqrstuúüvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚÜVWXYZ"
	C="0123456789*():¡!¿?%\"-;,.# "
	m = len(C)
	return B,C,m

def desencriptar(A):
	B,C,m = llave()
	aux = []
	if A == "":
		return A

	for j in A:
		if j < 0:
			aux.append(C[j])
		else:
			aux.append(B[j])
	salida = "".join(aux)

	return salida

def encriptar(cadena):
	A = cadena.strip()
	B,C,m = llave()
	n=len(A)
	x=[]
	if A == "":
		return A

	for i in range(n):
		D = B.find(A[i])
		if D == -1:
			D = C.find(A[i])
			if D == -1:
				D = -2
			else:
				D -= m
		x.append(D)
	return x



def main():
	i=input("Ingresa una cadena de caracteres: ")

	h=encriptar(i)
	print(h)
	print("Devolviendo")
	print(desencriptar(h))

if __name__ == '__main__':
	main()
