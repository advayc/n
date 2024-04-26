import math

def angle(a, b, c):
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    angle_A = math.degrees(math.acos(cos_A))
    
    print((str(round(angle_A)) + ' degrees'))

angle(3, 4, 5)
angle(4, 3, 5)  
angle(5, 4, 3) 
