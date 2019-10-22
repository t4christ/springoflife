# def addition(**kwargs):
#     kwargs["name"]="Temitayo"
#     print(kwargs)
# myict = {}
# mydict = {"number":"0708","age":"28","country":"nigeria","num":"008","state":"ogun"}
# mydit = {"numb":"0708","aged":"28","countri":"nigeria","numb":"008","stat":"ogun"}
# addition(**mydict)

# copdict = myict.update(**mydict)
# print(copdict)

# # for k,v in mydict.items():
# #     print(k , v, sep=" => ")
# # ctemp =[30,40,50,60,70]

# # print(tuple(map(lambda t: t/5,ctemp)))

# # from enum import Enum,unique,auto
# # @unique
# # class Fruit(Enum):
# #     APPLE = 1
# #     BANANA = 2
# #     ORANGE = 3
# #     TOMATO = 4
# #     PEAR = auto()

# # myFruit={}
# # myFruit[Fruit.BANANA] = " This is temitayo for python"
# # print(myFruit[Fruit.BANANA],Fruit.BANANA.value,Fruit.PEAR.name,Fruit.PEAR.value)

# class Person():
#     def __init__(self):
#         self.fname = "Temitayo"
#         self.lname= "Bakare"
#         self.age = "28"

#     def __repr__(self):
#         return "<Person ({0} {1} is {2} years old)".format(self.fname,self.lname,self.age)
    
#     def __str__(self):
#         return "(String {0} {1} is {2} years old".format(self.fname,self.lname,self.age)

#     def __bytes__(self):
#         val = "Person:{0} {1} is {2} years old ".format(self.fname,self.lname,self.age)
#         return bytes(val.encode('utf-8'))

# cls1 = Person()
# print(repr(cls1))
# print(str(cls1))
# print(bytes(cls1))

# class myColor():
#     def __init__(self):
#         self.red = 50
#         self.green = 75
#         self.blue = 100

    
#     def __getattr__(self,attr):
#         if attr == "rgbcolor":
#             return (self.red,self.green,self.blue)

#         elif attr == "hexcolor":
#             return "#{0:02x}{1:02x}{2:02x}".format(self.red,self.blue,self.green)
#         else:
#             raise AttributeError

#     def __setattr__(self,attr,val):
#         if attr == "rgbcolor":
#             self.red = val[0]
#             self.green = val[1]
#             self.blue = val[2]
#         else:
#             super().__setattr__(attr,val)
    
#     def __dir__(self):
#         return("red","green","blue","rgbcolor","hexcolor")


# cls1 = myColor()

# print(cls1)
# print(cls1.hexcolor)

# cls1.rgbcolor= (100,150,200)

# print(cls1.rgbcolor)
# print(cls1.hexcolor)


# class Point():
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y

#      def __repr__(self):
#          return "<Point x:{0},y:{1}>".format(self.x, self.y)

#      def __add__(self, other):
#          return Point(self.x + other.x, self.y + other.y)

#      def __sub__(self, other):
#          return Point(self.x - other.x, self.y - other.y)

#      def __iadd__(self, other):
#          self.x += other.x
#          self.y += other.y
#          return self


# # def main():
# p1 = Point(10, 20)
# p2 = Point(30, 30)
# print(p1, p2)

# p3 = p1 + p2
# print(p3)

# p4 = p2 - p1
# print(p4)

# p1 += p2
# print("I add {}".format(p1))
    


# main()

#     if __name__ == "__main__":
#         main()



# # class Employee():
# #     def __init__(self, fname, lname, level, yrsService):
# #         self.fname = fname
# #         self.lname = lname
# #         self.level = level
# #         self.seniority = yrsService

# #     def __ge__(self, other):
# #         if (self.level == other.level):
# #             return self.seniority >= other.seniority
# #         return self.level >= other.level


# #     def __gt__(self, other):
# #         if (self.level == other.level):
# #             return self.seniority > other.seniority
# #         return self.level > other.level


# #     def __lt__(self, other):
# #         if (self.level == other.level):
# #             return self.seniority < other.seniority
# #         return self.level < other.level


# #     def __le__(self, other):
# #         if (self.level == other.level):
# #             return self.seniority <= other.seniority
# #         return self.level <= other.level

# #     def __eq__(self, other):
# #         if (self.level == other.level):
# #             return self.seniority == other.seniority
# #         return self.level == other.level


# # def main():

# #     dept = []
# #     dept.append(Employee("Temitayo", "Bakare", 5, 9))
# #     dept.append(Employee("Ayodeji", "Bakare", 4, 12))
# #     dept.append(Employee("Damilare", "Bakare", 6, 6))
# #     dept.append(Employee("Titilayo", "Bakare", 5, 13))
# #     dept.append(Employee("Answer", "Adesanya", 5, 12))

# #     print(dept[0] > dept[2])
# #     print(dept[4] < dept[3])

# #     emps = sorted(dept)
# #     for emps in emps:
# #         print(emps.fname)

# # main()
# # import logging

# # def main():

# #     logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")
# #     logging.debug("This is a debug message")
# #     logging.info("This is a info message")
# #     logging.warning("This is a warning message")
# #     logging.error("This is a error message")
# #     logging.critical("This is a critical message")

# #     logging.info("Here's a {} variable an int:".format("string", 10))

# # main()

# # extData={'user' : 'bakaretemitayo7@gmail.com'}

# # def anotherFunction():
# #     logging.debug("This is a debug-level message",extra=extData)
# # def main():
# #     fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
# #     datestr = "%m/%d/%Y %I:%M:%S %p"
# #     logging.basicConfig(filename="output.log", level=logging.DEBUG, filemode="w", format=fmtstr, datefmt=datestr)
# #     logging.info("This is a info-level message",extra=extData)
# #     logging.warning("This is a warning-level message",extra=extData)

# # main()
# # anotherFunction()

# # arr_1 = [2,4,8,7,9]
# # arr_2 = [3,4,8,7,9]
# # arr_3 = [-10,4,8,7,21]


# # def add_twice(get_list):
# #     new_list={}
# #     for item in get_list:
# #         # print(10-item)
# #         if (10-item) in new_list:
# #             print(str(10-item) + "," + str(item))
# #             return
# #         else:
# #             new_list[item]=1
#     # print(new_list.keys())
    
            

# # add_twice(arr_3)




# evens = [2, 4, 6,8,10,12,14,16,18,20]
# odds = [1, 3, 5,7,9,11,13,15,17,18]


# evenSquared = list(map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
# print(result(10))


# # evenSquared = [e**2 for e in evens]
# # print(evenSquared)


# # evenSquared = [e**2 for e in odds if e > 3 and e < 17]
# # print(evenSquared)


# # class Computer:
#     # def __init__(self):
#         # self.age=20

#     # def update(self):
#         # self.age=30
#         # return self.age

# # c1 = Computer()
# # c1.update()
# # print(c1.age)
# #print address of the object
# # print(id(c1))



# ####### Python Factory Design Pattern ############

# BaseClass = type('BaseClass',(object,),{})

# @classmethod
# def Check1(self,myStr):
#      return myStr == "Ham"


# @classmethod
# def Check2(self,myStr):
#      return myStr == "SandWitch"
# C1 = type('C1',(BaseClass,),{'x':1,'Check':Check1})
# C2 = type('C2',(BaseClass,),{'x':30,'Check':Check2})

# def createFactory(myStr):
#      for cls in BaseClass.__subclasses__():
       
#          if cls.Check(myStr):
#              return cls()
       

# m = createFactory('Ham')
# v = createFactory('SandWitch')

# print(m.x,v.x,sep=' -- ')

# # def sort(seq):

# #     if len(seq) <= 1:
# #         return seq

# #     else:
# #         pivot =  seq[0]
# #         # print("pivot1",pivot,seq[0])
# #         # print("seqlen",len(seq))
# #         left, right = [],[]
# #         for x in seq[1:]:
# #             if x < pivot:
# #                 print("left",x)
# #                 left.append(x)
# #             else:
# #                 print("right",x)
# #                 right.append(x)
# #         # print("All together",sort(left),sort(right))
# #         return sort(left) + [pivot] + sort(right)
# # print(sort(['e','f','h','c','a','d','b','g']))

# ######### Python Class Method Decorator ###########
# # class MyClass:
# #     @classmethod
# #     def printHam(self):
# #         print("Ham")


# # MyClass.printHam()

# ############## Return the number of alphabet inputted ##################
# alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
# c  = input("Letter (a-z): ")
# print("C order",ord(c),ord('a'))
# n = ord(c) - ord('a') + 1
# n = alpha.get(c,'Sorry this is an invalid input')
# print("Its number is %d" % n)

# # first = input("First letter: ")
# # last = input("Last letter: ")

# # while first <= last:
# #     print(first, end='')
# #     first = chr(ord(first) + 1)
# # print()


# ############## Combine two lists into a dictionary ##############
# # from time import perf_counter
# # a = [1,2,3,4,5]
# # b = ['a','b','c','d','e']

# # c = {}
# # start = perf_counter()
# # c = dict(zip(b,a))
# # end = perf_counter() - start
# # print("Timer",end)
# # if len(a) == len(b):
# #     start = perf_counter()
# #     for i in range(len(a)):
# #         c[b[i]] = a[i]
# #     end = perf_counter() - start
# #     print("Timer2",end)    
# #     print(c)    
# # else:
# #     print("The two lists must be of equal lengths")


# # mac = {1,2,3,4,5,6,7,8,9,8}

# # mac_upt = [m for m in mac]

# # print(mac_upt)



# print({x:x**2 for x in range(10)})


# from time import perf_counter

# team1 = {'name':'peculiar','age':16,'country':'nigeria','state':'ogun','city':'abeokuta'}
# team2 = {'fname':'flourish','how_old':16,'nationality':'nigeria'}
# start = perf_counter()
# print({k:v for team in (team1,team2) for k,v in team.items() })
# end = perf_counter() - start

# print(end)

# import os

# path = os.path.abspath('./posts/urls.py')

# with open(path) as f:
#     print(f.read())

# for i in range(10):
#        count=0
#        for j in range(i):
#         count+=1
#         print(i * j,count)

# arr1 = [1,2,3]
# arr2 = [3,2,1]

# count = 0
# res = []
# for a in arr1:
#        if a < arr2[count] or a > arr2[count]:
#               res.append(1)       
#               count+=1
# print(res)
