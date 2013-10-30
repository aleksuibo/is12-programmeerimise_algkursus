def keskmine(*arvud):
    return sum(arvud)/(len(arvud))





def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    
    for i in range (0, number):
        fibonacci = fibonacci1(i)

        print (fibonacci)



def ruutvõrrand(a,b,c):

    import math
    
    valem1 = (b**2-4*a*c)
    if valem1 > 0: 
        valem1 = math.sqrt(valem1)
        valem1 = (-b+(valem1))
        valem1 = valem1/(2*a)
    else:
        valem1 = 'puudub'


    valem2 = (b**2-4*a*c)
    if valem2 > 0: 
        valem2 = math.sqrt(valem2)
        valem2 = (-b-(valem2))
        valem2 = valem2/(2*a)
    else:
        valem2 = 'puudub'

    print ("X1={} ja X2={}".format(valem1, valem2))
    
