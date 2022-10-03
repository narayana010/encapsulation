# encapsulation is the one of the concept of object oriented program.
#it describes the wraping or binding up of variables and methods that works under one unit.
#this can put restrictions on variables and methods and can prevent acidental mmodification of data

#class is the example of encapsulation it binds the all the data of variables and methods

#here we can bind the data by private variables and private methods

#we can specify veariables and methods as private by placing "__" before veriables and methods

# public method             #these can acess any where in the class

#private mwthos             #accessable in their own class start with two underscores("__")

#public variables           #these can acess any where in the class

#private variables          #acessable in their own class and in method if defined in method it can only acess by that
                            #method only

#example of a private variable

class myclass():

    #public variable
    public_variable=567

    #private variable
    __variable=123

    #method of class
    def method(self):
        print(self.__variable)
    print(__variable) #here we can acess private variable because it is inside of class

object=myclass()
object.method()

#print(myclass.__variable)   #here we cant acess private variable because it is out side of calss

print(myclass.public_variable)  #here we can acess public variable any where outside the class or inside the class

#we cant acess private variable out side the class

#example of private method

class encapsulaton():

    def __init__(self,marks,total_marks):

        self.marks=marks
        self.total_marks=total_marks

    #here we are creating private method
    def __percent(self):
        self.percent=self.marks/self.total_marks*100
        return self.percent

    #here we cant directly acess __percent(method) because it is a private method

    def percent1(self):

        return ("percentage is ",self.__percent())

percent2=encapsulaton(marks=590,total_marks=600)
print(percent2.percent1())

#example of acessing private variable

class private_variable():

    #private variable
    __private_variable1=24

    #public method

    def public_method(self,number):

        self.__private_variable1=number

    def display(self):
        print(self.__private_variable1)


object1=private_variable()
print(object1.display())





























































