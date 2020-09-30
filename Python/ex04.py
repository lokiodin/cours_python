# Regarde si le nombre est un nombre premier
from math import sqrt

def est_premier(x):
	"""
	Retourne si le nombre est premier

	Args:
		x: la valeur à tester

	Returns:
		est_premier(x): True or False
	
	>>> est_premier(2)
	True
	>>> est_premier(3)
	True
	>>> est_premier(4)
	False
	>>> est_premier(7)
	True
	>>> est_premier(13)
	True
	>>> est_premier(20)
	False
	"""

	for d in range(2, x):
		if x%d == 0 :
			# print(f"{x} = {d} * {x//d} : false")
			return False
	# print(f"{x} : True")
	return True

# Calcul du premier nombre non premier de la suite de Fermat 2**2**1 + 1
i = 0
while 1:
	if not est_premier(2**(2**i) + 1):
		print(f"Le premier nombre de Fermat non premier est {i}")
		break
	i += 1


# Calcul du premier nombre premier après n = 100000
def est_premier_apres(n):
	while 1:
		if est_premier(n):
			# print(f"Les premier nombre premier après n = 100000 est   :  {n}")
			return n
		n += 1
n = 100000
print(f"Les premier nombre premier après n = 100000 est   :  {est_premier_apres(n)}")

# Calcul du premier couple de nombre premier après n = 100000
n = 100000
while 1:
	p = est_premier_apres(n+1)
	pp = est_premier_apres(p+1)
	if (pp - p) == 2:
		print(f"Le premier couple de nombre premiers jumeaux est  ({p}, {pp})")
		break
	n  = p

# Calcul le premier nombre premier de Germain après n = 100000
n = 100000
while 1:
	if est_premier(n):
		if est_premier(2*n + 1):
			print(f"Le premier nombre premier de Germain après 100000  :  {n}")
			break
	n += 1