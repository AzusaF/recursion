def quadraticEquation(a,b,c):
    if a == 0: return 0
    discriminant = pow(b,2) - 4*a*c
    if discriminant > 0: return 2
    elif discriminant == 0: return 1
    else: return -2
