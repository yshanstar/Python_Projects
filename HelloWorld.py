print ("Hello World!")
print ("this is the first example!")

'''
print ("This is in comment")
'''
print ("This is out of the comment!")

i=20
if i>=22:
    print ("Here a > 21 !")
elif i>=21:
    print ("Here is a >= 21 !")
else:
    print ("else")

a = 10
def add(b):
    global a
    a += b
    print (a)
add(14)

for i in range(1, 10):
    add(12)

c = 1
while c < 20:
    print (c)
    c += 1

print ("This is B")
print (c)

myString = "abcdefghighabcdeabc"
print (myString.find('a'))
print (myString.count('a'))
print (myString[0:4])
print (myString[:-2])


myList = [8,7,6,5,4,3,2,1]
for i in myList:
    print (i)

myList.sort()

for i in myList:
    print (i)
