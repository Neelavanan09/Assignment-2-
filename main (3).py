Num = []
for x in range(1,11):
	Num.append(x)
print("The list of numbers from 1 to 10 = ", Num)
for index, i in enumerate(Num):
	if(i%2==0):
		del Num[index]
print("The list after deleting even numbers = ", Num)