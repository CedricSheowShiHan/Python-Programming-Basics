# introduction of if else statements

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# introduction of elif statements

age_new = 21 

if age_new < 13:
    print ("you are a child.")

elif age_new < 18:
    print ("You are a teenager.")

else:
    print ('Your age is greater than or equal to 18, therefore you are now an adult.')


# nested conditional statements

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0: #to check if theres a decimal, as it will usually have if its being divided by 2.
        print("The number is even.")
    else:
        print("The number is odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
