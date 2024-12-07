area_square=lambda side:side*side
area_rectangle=lambda length,breadth:length*breadth
area_triangle=lambda base,height:0.5*base*height
side=float(input("Enter the side of square in centimetres:"))
print("Area of Square :",area_square(side),"sq.cm")
length=float(input("Enter the length of rectangle in centimetres:"))
breadth=float(input("Enter the breadth of rectangle in centimetres:"))
print("Area of Rectangle :",area_rectangle(length,breadth),"sq.cm")
base=float(input("Enter the base of triangle in centimetres:"))
height=float(input("Enter the height of triangle in centimetres:"))
print("Area of Triangle :",area_triangle(base,height),"sq.cm")
