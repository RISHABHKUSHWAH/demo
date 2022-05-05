# # a = 2
# # b = 12
# # print(b/a)
# # print(b//a)
# # print(b%a)
# # print(id(a))
# # print(id(b))

# #####1
# # num = int(input("Enter number:-"))
# # for i in range(1,num):
# #     print("*"*i)
# # for i in range(num,1,-1):
# #     print("*"*i) 
# # 


# #2

# # num = int(input("Enter number:-"))
# # for i in range(1,num):
# #     print("*"*i)
# # for i in range(num,1,-1):
# #     print("*"*i)

# # num = int(input("Enter number:-"))
# # for i in range(1,num):
# #     print(" "*i,)
# # for i in range(num,1,-1):
# #     print(" "*i,)

# #******************************************************

# # num = int(input("Enter the number="))
# # j = 1
# # q = 0
# # a = num-1
# # for i in range(a,-1,-1):
# #     print(" "*i,end="")
# #     print("*"*j,end="")
# #     print("*"*q) 
# #     j+=1
# #     q+=1   
# # for i in range (1,num):
# #     print(" "*i,end="")
# #     print("*"*a,end="")
# #     print("*"*(a-1))
# #     a -=1

# #*************************************

# # num = int(input("Enter the number="))
# # j = 1
# # q = 0
# # a = num-1
# # for i in range(a,-1,-1):
# #     print("*"*i,end="")
# #     print(" "*j,end="")
# #     print(" "*q,end="")
# #     print("*"*i) 
# #     j+=1
# #     q+=1   
# # for i in range (1,num):
# #     print("*"*i,end="")
# #     print(" "*a,end="")
# #     print(" "*(a-1),end="")
# #     print("*"*i)
# #     a -=1

# # create a list of prime numbers
# #prime_numbers = [2, 3, 5, 7]

# # reverse the order of list elements
# #prime_numbers.reverse()


# #print('Reversed List:', prime_numbers)

# # Output: Reversed List: [7, 5, 3, 2]

# # p = {"a","a","c",1,2,3,4,65,7,8,9,4,3,2,1}
# #p.clear()
# # q ={"a",4,2}
# # print(q.issubset(p))
# # print(p)
# # print(type(p))

# # p = (1,2,3,4,5,6,7,1,2,3,4,5)
# # p[2] = 55
# # print(p[2])
# # print(p,type(p))

# # dic = {1:"one",2:"two",3:"three",4:"one"}
# # dic[4]="four"
# # print(dic)

# # name = "Rishabh"
# # age =20
# # print("my name is %s and my age is %d"%(name,age))

# # Python program to create a table

# from tkinter import *


# class Table:
	
# 	def __init__(self,root):
		
# 		# code for creating table
# 		for i in range(total_rows):
# 			for j in range(total_columns):
				
# 				self.e = Entry(root, width=20, fg='blue',
# 							font=('Arial',16,'bold'))
				
# 				self.e.grid(row=i, column=j)
# 				self.e.insert(END, lst[i][j])

# # take the data
# lst = [(1,'Raj','Mumbai',19),
# 	(2,'Aaryan','Pune',18),
# 	(3,'Vaishnavi','Mumbai',20),
# 	(4,'Rachna','Mumbai',21),
# 	(5,'Shubham','Delhi',21)]

# # find total number of rows and
# # columns in list
# total_rows = 6
# total_columns = 3

# # create root window
# root = Tk()
# t = Table(root)
# root.mainloop()


# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	#@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('renu', 1996)

# rishabh
#alkfskldfk
#f dsjnvdsnvnfd
#sjkdnjdfsgkjhnef#
#ksnflkjlk

print (person1.name,person1.age)
print (person2.name,person2.age)

# print the result
print (Person.isAdult(22))
