#variables and data types 

name = input("write your name =")            #string
age = "20"                                   #string change ho k string sa int ho ga
city = "Sheikupura"
department = "BS (IT) 5thsamester"
cgpa = 3.3                                   #float
is_pass = True                               #bool=true or false
print("wellcome",name)                       #simple print
print(age)
print(city)
print(department)
print(cgpa)

#type casting
age=int(age)                                 #string sa float 
print (type(age))


#operations in phyton
print("-- operations in phyton start --")
#Arithmatic operations
a=input("Enter the value of first number")
b=input("Enter the value of 2nd number")
a=int(a)
b=int(b)
print("The sum is =",a + b)   
print("The subtraction is ",a-b)  
print("Multliplication is =",a * b)   
print("The devision value is",a / b)   
print("The remainder is =",a % b) 

print("comparison operators start ")
age = 20
print(age >= 18)
print(age == 18)
print(age != 18)
print("-- comparison operators end --")

print("-- string method start --")
name = "subhan khalid"
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.replace("subhan", "Ali"))
print(len(name))
print("-- string method end --")


print("-- indexing in string start --")

name = "Subhan"
print(name[0])#is ka matlab hai k name ka 0 index print ho ga
print(name[1])
print(name[3])# is ka matlab hai k name ka 3 index print ho ga
print(name[-1])# is ka matlab hai k name ka last index print ho ga
print("-- indexing in string end --")

print("-- slicing start ")
name = "Mian Subhan Khalid"
print("original text is = Mian Subhan Khalid")
print(name[0:6])
print(name[7:13])
print(name[:6])
print(name[-6:])
print(name[::-1])
print("-- slicing is end --")