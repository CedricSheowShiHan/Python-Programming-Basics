#introduction to loops in python

range (10) # this will create a range of numbers from 0 to 9, which is 10 numbers in total.

for i in range(10):
    print (i) # this will print the numbers from 0 to 9, each on a new line.


for i in range(5, 10):
    print (i) # this will print the numbers from 1 to 9, each on a new line. The range starts at 1 and ends at 9, which is 9 numbers in total.

for i in range(1, 10, 2):
    print (i) 
# The range starts at 1 and ends at 9, with a step of 2, which means it will skip every second number.

for i in range(10, 0, -1):
    print (i)
# The range starts at 10 and ends at 1, with a step of -1

# strings 

str = 'Cedric Sheow is a Programmer'
for i in str:
    print (i)
    # this will print each character in the string 'Cedric Sheow is a Programmer' on a new line, including spaces and punctuation.


#while loop
count = 0 
while count  < 5: 
    print (count)
    count = count + 1

    #this outputs from 0 to 4, as the while loop continues to execute the loop 5 times from 0 to 4. 

count = 0

while count % 2 == 0:
    print (count)
    count = count + 1

#loop control statements

for i in range(10):
    if i == 5:
        break # this will exit the loop when i is equal to 5, so it will print the numbers from 0 to 4 and then stop.
    print (i)   

# pass statement

for i in range(5):
    if i == 3:
        pass
    print (i)


# nested loops

for i in range(3):
    for j in range(2):
        print (f"i: {i} and j:{j}")

# this is a nested loop, which means theres a for loop inside a for loop. 
# range(3) meaning the outer loop will run 3 times, with i = 0, 1 and then 2.
# for each value of i, the inner loop will run 2 times, with j = 0 and then 1.
# the output will be:
# i: 0 and j: 0
# i: 0 and j: 1
# i: 1 and j: 0
# i: 1 and j: 1
# i: 2 and j: 0
# i: 2 and j: 1

# Therefore the output will print() happens 3 x 2 = 6 times in total. 