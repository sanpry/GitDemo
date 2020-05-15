print("********************************")
print("1")
print("********************************")

file = open('test.txt')

for line in file.readlines(): #file.readlines() - Text values will be stored in a list
    print(line)

file.close()
print("********************************")
print("2")
print("********************************")
file = open('test.txt')
line = file.readline() #assign first line

while line != "": #when line is not empty
    print(line)
    line = file.readline() #assign next line

file.close()
print("********************************")
print("3")
print("********************************")

with open('test.txt', 'r') as reader: #r is read file or read mode
    content = reader.readlines()
    print(content)
    reversed(content)
    with open('test.txt', 'w') as writer: #w is write file or write mode
        for line in reversed(content):
            writer.write(line) #writes reversed values directly in file





