f = open('test.txt', 'r')
line = f.readline()
sum = 0
count = 0
while line != '':
    num = line.split(',')

    for i in num:
        sum += int(i)
        count += 1
    line = f.readline()
print("Average of all the numbers in the file test.txt is %f" %(sum/count))