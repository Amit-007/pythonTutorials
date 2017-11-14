

# IF Statements


print('Control Flow Statements : IF Statements')
x = int(input("Please enter a number : "))

if x < 0:
    x = 0
    print("X was negatie so its changed to 0")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print(x)


# For Loops

print("For Loops")

for num in range(0, 10):
    print(num, end=',')

words = ["Amit", "Bittu", "Zoey", "Python", "Swift"]

# Loop over a slice copy of the entire list.
for w in words[:]:
    if len(w) > 4:
        words.insert(0, w)

print(words)

for w in words:
    print(w, len(w))

# Range can also be used like this

for i in range(5):
    print(i, end=' # ')

for i in range(0, 100 , 20):
    print(i, end=' * ')

names = ["Bob Marley", "Jack Johnson", "Peter Parker", "Dr Bruce Banner", "Tony Stark", "Dr Hank Pim", "Bruce Wayne"]

for index in range(0, len(names)):
    print(index, names[index])

# OR

for index in range(len(names)):
    print(index, names[index])

# Print Range

print(range(10))


# BREAK AND CONTINUE STATEMENTS

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, '*', n//x)
            break

    else:
        print(n, "is a prime number")

# the else clause belongs to the for loop, not the if statement.)
# When used with a loop, the else clause has more in common with the
# else clause of a try statement than it does that of if statements:
# a try statement’s else clause runs when no exception occurs,
# and a loop’s else clause runs when no break occurs.


# Continue

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# Pass

class MyEmptyClass :
    pass

# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:



