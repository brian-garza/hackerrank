################################
####  Sorting Application   ####
################################

lower = ''
upper = ''
even = ''
odd = ''

string = sorted(input())

for i in string:
    if i.islower():
        lower += i
    elif int(i) % 2 != 0:
        odd += i
    elif i.isupper():
        upper += i
    else:
        even += i

print(lower + upper + odd + even)