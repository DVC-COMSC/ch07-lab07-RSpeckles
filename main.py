
inputvalues = input()
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
evenlist = []
i = 0
while i < len(numbers1):
	evenlist.append(numbers1[i])
	numbers1.pop(i)
	i += 1

print (evenlist)
print (numbers1)
