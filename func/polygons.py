import math
def rectangle(l,w):
    sum = l*w
    return sum

def circle(l,w):
    sum = math.pi * r**2
    return sum

def triangle(h,b):
    sum = (h*b) / 2
    return sum

shape = input('what shape u want: ')

if shape == 'triangle' or 'Triangle':
    h = int(input('enter height: '))
    b = int(input('enter base: '))
    print(triangle(h,b))
elif shape == 'circle' or 'Circle':
    r = int(input('enter radius: '))
    print(circle(r))
elif shape == 'rectangle' or 'Rectangle':
    print(rectangle(l,w))
    l = int(input('enter length: '))
    w = int(input('enter width: '))
else:
    print('enter valid shape')
