import math
def solve_quadratic(a,b,c):
    if (math.pow(b,2) - (4*a*c)) < 0:
        return
    x1 = (-b + math.sqrt(math.pow(b,2) - (4*a*c))) / (2*a)
    x2 = (-b - math.sqrt(math.pow(b,2) - (4*a*c))) / (2*a)
    if x1 == x2:
        return x1
    else:
        return (x1,x2)