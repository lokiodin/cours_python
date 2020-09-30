# Regarde si le nombre est un nombre premier
from math import sqrt

def est_premier(x):
	for d in range(2, x):
		if x%d == 0 :
			print(f"{x} = {d} * {x//d} : false")
			return
	print(f"{x} : True")

def syracuse(s):
	"""
	Temps de vol k : tel que uk = 1 (pour s = 15, k = 17)
	Temps de vol altitude : tel que u(k+1) <= u0 où u0=s. (ex : pour s = 15, k = 10)
	Altitude max : val max de toutes les val rencontrées
	"""
	tps_vol = 0
	u0 = s
	tps_vol_alt = 0
	alt_max = s
	
	while s != 1:
	    if s % 2 == 0:
	        s = s // 2
	    else:
	        s = 3 * s + 1
	    tps_vol += 1
	    if s > u0: tps_vol_alt += 1
	    if s > alt_max:
	    	alt_max = s
	    # print(s, end=" ")
	# print()
	return tps_vol, tps_vol_alt-1, alt_max

# est_premier(731)
# est_premier(733)

# print(syracuse(15))
# print(syracuse(127))

for i in range(1, 10000):
	tmp = syracuse(i)
	print(f"n = {i} :\n\tTemps de vol : {tmp[0]}\n\tTemps de vol altitude : {tmp[1]}\n\tAltitude max : {tmp[2]}")