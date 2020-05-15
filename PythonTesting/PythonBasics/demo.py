val = [1, 2, 3, 4, "rahul"]

print(val[1])
print(val[-1])

val.insert(2, "shetty")
print(val)

val.append("last")
print(val)

del val[-1]
print(val)

val[-1] = "RAHUL"
print(val)

print("*************************************")

dic = {"a": 2, 4: "rah"}

print(dic[4])

dict = {}

dict["fname"] = "swetha"
dict["lname"] = "gj"

print(dict)

print("*************************************")

print("hello world")

print("*************************************")

a = "hello morning"
if a == "hello morning":
    print("a is matching")
    print("2nd line")
else:
    print("a is not matching")

print("if else condition is done")

print("*************************************")

obj = [2, 5, 6, 7, 8]
for i in obj:
    print(i)
print("*************************************")

summation = 0
for j in range(1, 6):
    summation = summation + j

print(summation)

print("*************************************")
# skip every 2 numbers in range 1 to 10
for k in range(1, 10, 2):
    print(k)

print("*************************************")
# skip first index, prints from 0 to 9
for m in range(10):
    print(m)

print("*************************************")

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)

    it = it - 1
print("*************************************")

def greetMe():
    print("good morning")


greetMe()

print("*************************************")

def goodMe(name):
    print("good morning "+name)


goodMe("swetha")
print("*************************************")

def AddInt(a, b):
    print(a+b)


AddInt(3, 4)

print("*************************************")

def AddInt(a, b):
    return a+b


print(AddInt(3, 4))

print("*************************************")
