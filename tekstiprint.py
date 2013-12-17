import sys
def fn(x,y,tekst):
        sys.stdout.write("\033["+str(y)+";"+str(x)+"H"+tekst)
sys.stdout.write("\033[2J")
fn(5,5,"test")
print
