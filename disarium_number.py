disarium = 0
num = int(input("Enter a Number :\n"))
strnum = str(num)
for i in range(len(strnum)) :
    disarium += int(strnum[i])**(i+1)

if num==disarium :
    print(f"{num} is a disarium number.")

else :
    print(f"{num} is not a disarium number.")
