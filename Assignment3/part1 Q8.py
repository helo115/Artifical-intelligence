#8.Write a function to compute the area and circumference of the circle and return the computed results.
r=int(input("enter a radius"))
def area (r):
    area=3.14*r*r
    circumference=2*3.14*r
    return area, circumference
hi=area(r)
print(hi)
