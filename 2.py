radius=int(input("enter radius"))
height=int(input("Enter height"))
def vol(radius,height):
    v=3.14*radius*radius*height
    print(v)

def surf(radius,height):
    s=((2*3.14*radius)*height)+((3.14*radius**2)*2)
    print(s)
vol(radius,height)
surf(radius,height)
