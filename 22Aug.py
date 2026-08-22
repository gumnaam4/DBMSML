'''marks=[56,76,98,23,88,70]
passed=[]
for m in marks:
    if m>=40:
        passed.append(m)
print(passed)'''


#List comprehension
'''passed=[m for m in marks if m>=40]
print(passed)'''


#Normal Function
def cube(x):
    return x*x*x

print(cube(3))


#Lambda Function 
