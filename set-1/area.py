def area(shape):
    match shape:
        case 'circle':
            r=int(input('enter the radius:'))
            return 3.14*r**2
        case 'rectangle':
            l=int(input('enter the length of the rectangle:'))
            b=int(input('enter the breadth of the rectange:'))
            return l*b 
        case _:
            return 'enter the proper shape'
shape=input('enter the shpae of the area we want to find:')
print(area(shape))