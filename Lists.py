women = [ "Amanda" , "Aprille" , "Cindy" , "Dorothy" , "Jess" ]

#prints above
print (women)
print ()

#prints number of things in list
print (len(women))
print ()

#checks if something is in the list (true/false)
print ("Jillian" in women)
print ("Dorothy" in women)
print ()

#print numbers in sequence
numbers = [1,4,2,4,6]

for num in numbers:
    print (num)

print ()

for i in range(len(numbers)):
    print(numbers[i])
print ()

for i in range (3):
    print (numbers[i])
print ()

for i in range(5):
    print (numbers[i])

#STRINGS

name = "Jillian!"
#prints number of letters in string
print (len(name))
print ()

#checks for letters in the string
print ("ian" in name)
print ()

#prints certain letter with index
print(name[4])
print ()

#prints range of them in a loop up to the end
for i in range(8):
    print (name[i])

print ()

#find the average

age = [5,12,3,56,24,78,1,15,44]
total = 0

for i in range (8):
    total += age[i]

print (total/len(age))
