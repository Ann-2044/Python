import graphics.rectangle  as rect
import graphics.circle as circ
import graphics.graphics_3d.cuboid  as cub
import graphics.graphics_3d.sphere as sph
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
print("area of rectangle:",rect.area(length,breadth))
print("perimeter of rectangle:",rect.perimeter(length,breadth))
radius=int(input("enter the radius of circle:"))
print("area of circle :",circ.area(radius))
print("perimeter of circle :",circ.perimeter(radius))
length=int(input("enter the length of cuboid:"))
width=int(input("enter the breadth of cuboid:"))
height=int(input("enter the height of cuboid:"))
print("area of cuboid :",cub.surface_area(length,breadth,height))
print("volume of cuboid:",cub.volume(length,breadth,height))
radius=int(input("enter the radius of sphere:"))
print("area of sphere :",sph.surface_area(radius))
print("volume  of sphere :",sph.volume(radius))
