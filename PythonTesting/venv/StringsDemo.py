str = "RahulShettyAcademy.com"
str1 = " consulting firm "

print(str[1]) #index
print(str[0:5]) #range
print(str+str1) #concatenation
print("********************")
var = str.split(".") #split and save into list
print(var)
print(var[1]) #call values from list using index

print("********************")
str3 = "Rahul"
print(str3 in str) #returns true

print("********************")
str4 = ' great '
print(str4.strip()) #removes white spaces
print(str4.lstrip()) #removes white spaces on left
print(str4.rstrip()) #removes white spaces on right


