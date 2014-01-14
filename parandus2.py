def joonista(x, y, sisu):
	print "\033[" + str(y) + ";" + str(x) +"H" + str(sisu)
	
def kast(x, y, laius, korgus):
	a = 0
	
	while a < laius:
		joonista(x+a, y, "#")
		joonista(x+a, y+korgus, "#")
		a = a + 1
		
	b = 0
	while b < korgus+1:
		joonista(x, y+b, "#")
		joonista(x+laius, y+b, "#")
		b = b + 1
		
kast(3, 3, 10, 10)

from random import randint
import sys


def tarnid(x,y, txt):
        a=0
        while a<100:
                x=randint(0,70)
                y=randint(0,20)
                sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + txt)
                a=a+1
tarnid(70,20, "*")
