number = int(input('Enter a number to see its multiplication table: '))
for x in range(1,11):
    for i in range (1,11) :
        opration = (x * number)
    print (f"{x} * {number} = {opration}")