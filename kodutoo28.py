#####################1
import math

def otsinumber(allikas):
	vaste = 0

	for i in allikas:
		if i.isdigit():
			vaste = 1
			break

	return vaste

sisestus = input('Sisestage tekst: ')

if otsinumber(sisestus) and sisestus.islower():
	print ('v2iksed t2hed ja numbrid')
elif not otsinumber(sisestus) and sisestus.islower():
	print ('v2iksed t2hed ja numbriteta')
elif otsinumber(sisestus) and sisestus.isupper():
	print ('suured t2hed ja numbrid')
elif not otsinumber(sisestus) and sisestus.isupper():
	print ('suured t2hed ja numbriteta')
else:
	if otsinumber(sisestus):
		print ('suured ja v2iksed t2hed ning numbrid')
	else:
		print ('suured ja v2iksed t2hed ja numbriteta')

######################2

number1 = input('Sisesta esimene number: ')
number2 = input('Sisesta teine number: ')

number1 = int(number1)
number2 = int(number2)

a = 0
kokku = abs(number1-number2)
vastus = 0

while a <= kokku:
	a = a + 1

	if a % 3 == 0:
		vastus = vastus + 1

print ('Arvuvahemikul '+str(number1)+' - '+str(number2)+' on '+str(vastus)+' 3-ga jaguvat arvu')
