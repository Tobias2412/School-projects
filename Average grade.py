num = int(input("how many grades do you have:"))

totalgrade = 0

for i in range(num):
    totalgrade += int(input("write your grade here: "))

print(totalgrade/num)