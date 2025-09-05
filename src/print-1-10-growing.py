
# Print the numbers described in the exercise
for i in range(1, 11):
    for j in range(1, i+1):
        if j == 10:
            print(j)
        else:
            print( j, end = ' ')

    print('') 