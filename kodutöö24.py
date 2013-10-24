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



    
