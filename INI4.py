# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

a = 100
b = 200

sum = 0

for i in range(a, b+1):
    if i%2 == 1:  #check for odd # % denotes remainder
        sum += i
print(sum)

 