#tuples are also similar to list 
#Use parentheses to create Tuples

#Example
my_tuples = (1,2,3,4,5)
print(my_tuples)

#Acces Tuples elements using indexing 

#example
my_tuples2 = (1,2,3,4,5)
print(my_tuples2[2])

#there are two tuples methods
#Count()
#Index()


#here is a count method
my_tuples = (1, 2, 3 , 3, )
print(my_tuples.count(3))

#here is a index method
my_tuples = (1, 2,4, 3 , 3, )
print(my_tuples.index(3))

#packing and unpacking 
my_tuples3 = ("apple","banana","orange",)
fruit1, fruit2, fruit3 = my_tuples3
print(fruit1)