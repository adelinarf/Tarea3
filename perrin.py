import numpy as np
import math

def power(M,n):
	if n<=1:
		return M 
	else:
		P = power(M, math.floor(n/2))
		if n % 2 == 0:
			return P*P 
		else:
			return P*P*M
#O(nlogn)
def numerosDePerrin(N):
	E = np.matrix([[0, 1, 0], [0, 0, 1], [1, 1, 0]])
	B = np.matrix([[P(0)],[P(1)],[P(2)]])
	mul = power(E,N)*B 
	return (mul.item(0))

#Version recursiva
def P(n):
	if n==0:
		return 3
	elif n==1:
		return 0
	elif n==2:
		return 2
	elif n>=3:
		return P(n-2)+P(n-3)

def main():
	z = input("Ingresa un número para calcular el número de Perrin:")
	print(numerosDePerrin(int(z)))

main()

