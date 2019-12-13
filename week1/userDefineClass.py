import math
# class Point:
#     """ point class will be used to manupulating the x,y"""
#     ## constructor goes here

#     def __init__(self):
#         self.x = 0
#         self.y = 0

# point1 = Point()
# point2 = Point()

# ## setting the attributes


# point1.x = 5
# point2.x = 10

# print (point1.x)
# print (point2.x)


# class Point():
#     def getx(self):
#         return self.x


# point1 = Point()
# point2 = Point()

# ## creating the attribute

# point1.x = 5
# point2.x = 10


# print (point1.getx())
# print (point2.getx())



## adding parameter to the Constructor

# class Point:

#     def __init__(self,intX,intY):
#         self.x = intX
#         self.y = intY

# p = Point(5,10)

# print(p)

# class Point:
#     def __init__(self,intX,intY):
#         self.x = intX
#         self.y = intY

#     ## apply method
#     ## this is the getter

#     def getx(self):
#         return self.x

#     def gety(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x**2)+(self.y**2))**.5

# ## inti the object
# p = Point(7,6)

# print(p.getx())
# print(p.gety())
# print (p.distanceFromOrigin())



# import math

# class point:
#     def __init__(self,intX,intY):
#         self.x = intX
#         self.y = intY

#     ## gette 

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return ((self.x)**2+(self.y**2))**.5

#     ### in this function we are foint to use self
#     #### for one function and other for the instance function

#     def distance(self,obj):
#         xdiff = obj.getX()-self.getX()
#         ydiff = obj.getY()-self.getY()
#         dist = math.sqrt(xdiff**2+ydiff**2)
#         return dist

# # functional way of doinr this

# def distanceFromEachOther(point1,point2):
#     xdiff = point2.getX()-point1.getX()
#     ydiff = point2.getY()-point1.getY()
#     disttance = math.sqrt(xdiff**2+ydiff**2)
#     return disttance

# p = point(4,3)
# q = point(0,0)

# ### adding a object to anothrt class

# print(distanceFromEachOther(p,q))

# print (p.distance(q))


### chaing the object to  a string

# class Point:

#     def __init__(self,intX,intY):
#         self.x = intX
#         self.y = intY
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y

#     def distanceFromOrigin(self):
#         return math.sqrt((self.x)**2+(self.y)**2)

#     ## chaning the str

#     def __str__(self):
#         return "x={},y={}".format(self.x,self.y)

# p = Point(7,6)

# print(p)


# class Cereal:
#     def __init__(self,name,brand,fiber):
#         self.name = name
#         self.brand = brand
#         self.fiber = fiber
        
#     def __str__(self):
#         return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,int(self.fiber))
    
# c1 = Cereal("Corn Flakes","Kellogg's",2)
# c2 = Cereal("Honey Nut Cheerios","Honey Nut Cheerios",3)

# print(c1)
# print(c2)

## instance and reeturh value

# class Point:
#     def __init__(self,intX,intY):
#         self.x = intX
#         self.y = intY
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#     def distanceFromorigin(self):
#         return ((self.x**2)+(self.y**2))**.5

#     def __str__(self):
#         return "x = {}, y = {}".format(self.x,self.y)


#     ## this will be done by one class and another object
#     ## we create the two obejst and one will be provided

#     def halfway(self,target):
#         mx = (self.x+target.x)/2
#         my = (self.y+target.y)/2
#         return Point(mx,my)
# ## make a point now

# p = Point(3,4)
# q = Point(5,12)

# ## because we just send these two numern to a object
# ## we can fetch it with the getter

# mid = p.halfway(q)

# print(mid)
# # print(mid.getX())
# # print(mid.getY())


# ## lanmda function 
# ## using lambda function fr sorting
# L = ["Cherry","Apple","Blueberry"]
# print(sorted(L))


# print(sorted(L,key=len))

# ## we actually prvide the function that are goinf to used
# ## we can see the it will be sorted with respect to length



# ## it will be sorted using this lambda function
# ## which is a len function
# ## you can use your custom function
# print (sorted(L,key=lambda x: len(x)))


## can you sort a object??

# class Fruit():
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price 
# L = [Fruit("Cherry",10),Fruit("Apple",5),Fruit("Blueberry",20)]


# ## this is  list of objests
# print(L)

# for f in sorted(L,key=lambda x:x.price ):
#     print (f.name)


## sorted by priority

# class Fruit():
#     def __init__(self,name,price):
#         self.name = name 
#         self.price = price 

#     ## make a function for the lambda
#     ## or make a function for the sorted 
#     def sort_priority(self):
#         return self.price 

# L = [Fruit("Cherry",10),Fruit("Apple",5),Fruit("Blueberry",20)]

# for f in sorted(L,key=lambda x:x.sort_priority()):
#     print(f.name)

# class Point:
#     """ Point class for representing and manipulating x,y coordinates. """

#     printed_rep = "*"

#     def __init__(self, initX, initY):

#         self.x = initX
#         self.y = initY

#     def graph(self):
#         rows = []
#         size = max(int(self.x), int(self.y)) + 2
#         for j in range(size-1) :
#             if (j+1) == int(self.y):
#                 special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
#                 rows.append(special_row)
#             else:
#                 rows.append(str((j+1) % 10))
#         rows.reverse()  # put higher values of y first
#         x_axis = ""
#         for i in range(size):
#             x_axis += str(i % 10)
#         rows.append(x_axis)

#         return "\n".join(rows)


# p1 = Point(2, 3)
# p2 = Point(3, 12)
# print(p1.graph())
# print()
# print(p2.graph())



# class Point:

#     def __init__(self,initX,initY):
#         self.x = initX
#         self.y = initY

#     def distanceFromOrigin(self):
#         return ((self.x**2)+(self.y**2)) ** 0.5

#     def move(self,dx,dy):
#         self.x = self.x + dx 
#         self.y = self.y + dy


## testing the class

# To test a user-defined class, you will create test cases that check whether instances are created properly, and you will create test cases for each of the methods as functions, by invoking them on particular instances and seeing whether they produce the correct return values and side effects, especially side effects that change data stored in the instance variables. To illustrate, we will use the Point class that was used in the introduction to classes.

# To test whether the class constructor (the __init__) method is working correctly, create an instance and then make tests to see whether its instance variables are set correctly. Note that this is a side effect test: the constructor method’s job is to set instance variables, which is a side effect. Its return value doesn’t matter.

# A method like distanceFromOrigin in the Point class you saw does its work by computing a return value, so it needs to be tested with a return value test. A method like move in the Turtle class does its work by changing the contents of a mutable object (the point instance has its instance variable changed) so it needs to be tested with a side effect test.

# Try adding some more tests in the code below, once you understand what’s there.


# class Bike:
#     def __init__(self,color,price):
#         self.color = color
#         self.price = float(price)
# testOne = Bike('blue',89.99)
# testTwo = Bike('purple',25.00)
# print (testOne)
# print (testTwo)


# class AppleBasket:
#     def __init__(self,apple_color,quantity):
#         self.apple_color = apple_color
#         self.apple_quantity = int(quantity)

#     def increase(self):
#         self.apple_quantity+=1

#     def __str__(self):
#         return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)
# p1 = AppleBasket('red',4)

# p2= AppleBasket('blue',50)
# print (p1)
# print (p2)

# class Bike:
#     def __init__(self,color,price):
#         self.color = color 
#         self.price = float(price)

# testOne = Bike('blue',89.99)
# testTwo = Bike('purple',25.0)


class BankAccount:
    def __init__(self,name,amt):
        self.name = str(name) 
        self.amt = int(amt) 

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name,self.amt)

t1 = BankAccount('Bob',100)
print(t1)